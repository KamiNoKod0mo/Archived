<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1,maximum-scale=1">
	<title>Login</title>
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
			<p>User Login</p>
			<form method="post">
				<img src="<?php echo INCLUDE_PATH_STATIC ?>imgs/email.png">
				<input type="email" name="email" placeholder="Email">
				<img style="top: 38%;" src="<?php echo INCLUDE_PATH_STATIC ?>imgs/lock.png">
				<input type="password" name="password" placeholder="Password">
				<input type="submit" name="submit" value="Login">
				<input type="hidden" name="login">
			</form>
		</div>
	</section>

	<section class="center__link">
		<div class="container">
			<p>To create a new account <a href="<?php echo INCLUDE_PATH?>registrar">Click Here</a></p>
		</div>
	</section>

</body>
</html>