<?php
	
	namespace classes\Controllers;

	class PerfilController{


		public function index(){
			if(isset($_SESSION['login'])){

				if(isset($_POST['atualizar'])){
					$pdo = \classes\MySql::connect();
					$nome = strip_tags($_POST['nome']);
					$senha = $_POST['senha'];

					if($nome == '' || strlen($nome) < 3){
						\classes\Utilidades::alerta('Você precisa inserir um nome...');
						\classes\Utilidades::redirect(INCLUDE_PATH.'perfil');
					}

					

					if($senha != ''){
						$senha = \classes\Bcrypt::hash($senha);
						$atualizar = $pdo->prepare("UPDATE usuarios SET nome = ?, senha = ? WHERE id = ?");
						$atualizar->execute(array($nome,$senha,$_SESSION['id']));
						$_SESSION['nome'] = $nome;
						
						
					}else{
						
						$atualizar = $pdo->prepare("UPDATE usuarios SET nome = ?WHERE id = ?");
						$atualizar->execute(array($nome,$_SESSION['id']));
						$_SESSION['nome'] = $nome;
						
						
					}

					

					if($_FILES['file']['tmp_name'] != ''){
						$file = $_FILES['file'];
						$fileExt = explode('.',$file['name']);
						$fileExt = $fileExt[count($fileExt) - 1];
						
						if($fileExt == 'png' || $fileExt == 'jpg' ||$fileExt == 'jpeg'){
							//Formato válido.
							//Validar tamanho.
							$size = intval($file['size'] / 1024);
							if($size <= 300){
								$uniqid = uniqid().'.'.$fileExt;
								$atualizaImagem = $pdo->prepare("UPDATE usuarios SET img = ? WHERE id = ?");
								$atualizaImagem->execute(array($uniqid,$_SESSION['id']));
								$_SESSION['img'] = $uniqid;
								move_uploaded_file($file['tmp_name'],'/home/admin/projs/index/web_php/projeto/uploads/'.$uniqid);
								\classes\Utilidades::alerta('Seu perfil foi atualizado junto com a foto!');
								
								\classes\Utilidades::redirect(INCLUDE_PATH.'perfil');

								
							}else{
								\classes\Utilidades::alerta('Erro ao processar seu arquivo.');
								\classes\Utilidades::redirect(INCLUDE_PATH.'perfil');
							}
						}else{
							\classes\Utilidades::alerta('Erro ao processar seu arquivo.');
							\classes\Utilidades::redirect(INCLUDE_PATH.'perfil');
						}
					}

					\classes\Utilidades::alerta('Seu perfil foi atualizado com sucesso!');
					\classes\Utilidades::redirect(INCLUDE_PATH.'perfil');




				}


				\classes\Views\MainView::render('perfil');
			}else{
				\classes\Utilidades::redirect(INCLUDE_PATH);
			}
			
		}

	}

?>