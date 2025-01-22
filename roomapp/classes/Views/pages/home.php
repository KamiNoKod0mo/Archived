<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
	<title>Home</title>
	<link rel="stylesheet" type="text/css" href="<?php echo INCLUDE_PATH_STATIC ?>css/style2.css">
</head>
<body>
	<?php
		// Realiza a consulta para obter as informações das salas
		$query = \classes\MySql::connect()->prepare("SELECT criador, npart, hash FROM sala");
		$query->execute();

		// Recupera os resultados
		$rooms = $query->fetchAll();
	?>
	<header class="home">
		<nav class="home__title">
			<h1>Salas Onlines Disponives</h1>		
		</nav>
	</header>
	<a href="<?php echo INCLUDE_PATH ?>?loggout">loggout</a>
	<section class="box">
		<div class="box__create">
			<a href="<?php echo INCLUDE_PATH ?>room"><h3>Criar sala</h3></a>
		</div>
		<div class="box__container">
			<?php foreach ($rooms as $room): ?>
        <div class="box__room">
            <!-- Exibe o título com o hash (URL da sala) -->
            <a href="/roomapp<?php echo $room['hash']; ?>"><h3>Room <?php echo $room['hash']; ?></h3></a>
            
            <!-- Exibe o nome do criador -->
            <p>Criador: <?php echo $room['criador']; ?></p>
            
            <!-- Exibe o número de participantes -->
            <p>Participantes: <?php echo $room['npart']; ?></p>
        </div>
    <?php endforeach; ?>
		</div>
	</section>
	
	
</body>
<script type="text/javascript">
	sessionStorage.setItem('clicked', 'false');
</script>
</html>