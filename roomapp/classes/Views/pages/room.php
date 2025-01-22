<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
	<title>VideoChat</title>
	<link rel="stylesheet" type="text/css" href="<?php echo INCLUDE_PATH_STATIC ?>css/style2.css">
	<script src='https://cdn.scaledrone.com/scaledrone.min.js'></script>
</head>
<body>


	<header class="home">
		<nav class="home__title">
			<h1>Salas hash</h1>		
		</nav>
	</header>

	<section  class="video">
		<div class="video__remote">
			<video id="remoteVideo" autoplay playsinline></video>
			<p id="remote"></p>
		</div>

		<div class="video__local">
			<video id="localVideo" autoplay muted playsinline></video>
			<p id="local"></p>
		</div>
		<form method="post">
			<input type="submit" name="comp"  value="Compartilhar">
			<input type="hidden" id="criador" name="criador" value="">
			<input type="hidden" id="roomName" name="roomName" value="">
		</form>
		<form method="post">
			<input type="submit" name="num"  value="Encerrar">
			<input type="hidden" id="roomName2" name="roomName2" value="">
		</form>
	</section>

	
</body>
<script>
		// Solicita o nome do usuário local
		const localName = "<?php echo $_SESSION['nome']; ?>";
		let remoteName = ""; // Nome do usuário remoto

		let lp = document.getElementById('local');
		lp.innerHTML = localName;

		document.getElementById('criador').value = localName;

		let rp = document.getElementById('remote');

		if (!location.hash) {
			location.hash = Math.floor(Math.random() * 0xFFFFFF).toString(16);
		}

		const roomHash = location.hash.substring(1);
		const drone = new ScaleDrone('t2e3HEL2UP3URpRE')
		const roomName = 'observable-'+roomHash;

		document.getElementById('roomName').value = '/room#'+roomHash;
		document.getElementById('roomName2').value = '/room#'+roomHash;

		const configuration = {
			iceServers:[
				{
					urls: 'stun:stun.l.google.com:19302'
				}
			]	
		}
		let room;
		let pc;
		let number = 0;

		function onSuccess(){};

		function onError(error) {
			console.log(error);
		};

		drone.on('open', error => {
            if (error) return console.log(error);
            room = drone.subscribe(roomName);

            room.on('open', error => {});

            room.on('members', members => {
                console.log("Conectado");
                console.log('Conexões abertas: ' + members.length);

                number = members.length - 1;
                const isOfferer = members.length >= 2;
                startWebRTC(isOfferer);

                sendMessage({ name: localName });
            });
        });

		function sendMessage(message){
			drone.publish({
				room: roomName,
				message
			})
		}

		function startWebRTC(isOfferer){
			pc = new RTCPeerConnection(configuration);
			pc.onicecandidate = event =>{
				if (event.candidate) {
					sendMessage({'candidate':event.candidate});
				}
			};

			if(isOfferer){
				pc.onnegotiationneeded = () =>{
					pc.createOffer().then(localDescCreated).catch(onError);
				}
			}

			pc.ontrack = event =>{
				const stream = event.streams[0];

				if (!remoteVideo.srcObject || remoteVideo.srcObject.id !== stream.id) {
					remoteVideo.srcObject = stream;
				}
			}
			navigator.mediaDevices.getUserMedia({
				audio: true,
				video: true,
			}).then(stream => {
				localVideo.srcObject = stream;
				stream.getTracks().forEach(track=>pc.addTrack(track,stream))
			},onError)

			room.on('member_leave',function(member){
				//Usuário saiu!
				remoteVideo.srcObject = null; // Remove vídeo remoto
				rp.innerHTML = ""; // Remove o nome do usuário remoto
			})

			room.on('data',(message, client)=>{

				if(client.id === drone.clientId){
					return;
				}
				
				if (message.name) {
					// Recebe e exibe o nome do usuário remoto
					remoteName = message.name;
					//console.log("Usuário remoto: " + remoteName);
					rp.innerHTML = remoteName;
				}

				if(message.sdp){
					pc.setRemoteDescription(new RTCSessionDescription(message.sdp), () => {
						if(pc.remoteDescription.type === 'offer'){
							pc.createAnswer().then(localDescCreated).catch(onError);
						}
					}, onError)
				}else if(message.candidate){
					pc.addIceCandidate(
						new RTCIceCandidate(message.candidate), onSuccess, onError
					)
				}

			})


		}

		function localDescCreated(desc){
			pc.setLocalDescription(
				desc, () => sendMessage({'sdp': pc.localDescription}), onError
			);
		}
		window.addEventListener('beforeunload', function(event) {
            // Aqui você pode executar a ação que deseja quando a aba for fechada ou o navegador for fechado

            
        });


		
    
		

	</script>
</html>