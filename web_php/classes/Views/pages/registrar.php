<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>registro na Rede Social</title>
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>	
	<link href="https://fonts.googleapis.com/css2?family=Montserrat:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">

	<link rel="stylesheet" type="text/css" href="<?php echo INCLUDE_PATH_STATIC ?>estilos/style.css">
</head>
<body>
	<div class="sidebar"></div>
	<div class="form-container-login">
		<div class="logo-chamada-login">
			<img src="<?php echo INCLUDE_PATH_STATIC ?>images/logodanki.svg">
			<p>Conecte-se com seus amigos e expanda seus aprendizados com a rede social Danki Code.</p>
		</div>
		<div class="form-login">
			<h3 style="text-align: center;">Crie sua conta</h3>
			<form method="post">
				<input type="text" name="nome" placeholder="Seu nome... ">
				<input type="text" name="email" placeholder="Email... ">
				<input type="password" name="senha" placeholder="Senha... ">
				<input type="submit" name="acao" value="registrar!">
				<input type="hidden" name="registrar" value="registrar">
			</form>
		</div>

	</div>
</body>
</html>