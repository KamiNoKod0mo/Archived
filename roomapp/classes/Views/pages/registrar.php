<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1,maximum-scale=1">
	<title>Registrar</title>
	<link rel="stylesheet" type="text/css" href="<?php echo INCLUDE_PATH_STATIC ?>css/style.css">
</head>
<body>
	<header>
		<div class="container">
			<h2>Welcome to the website</h2>
		</div>
	</header>
 	
	<section class="">
		<div class="container center__box">
			<p>User Registration</p>
			<form method="post">
				<img src="<?php echo INCLUDE_PATH_STATIC ?>imgs/user.png">
				<input type="text" name="username" placeholder="Username">
				<img src="<?php echo INCLUDE_PATH_STATIC ?>imgs/lock.png">
				<input type="password" name="password" placeholder="Password">
				<img src="<?php echo INCLUDE_PATH_STATIC ?>imgs/email.png">
				<input type="email" name="email" placeholder="Email">
				<input type="submit" name="submit" value="Register">
				<input type="hidden" name="registrar" value="registrar">
			</form>
		</div>
	</section>

	<section class="center__link">
		<div class="container">
			<p>You have a account? <a href="<?php echo INCLUDE_PATH ?>home">Click Here</a></p>
		</div>
	</section>

</body>
</html>