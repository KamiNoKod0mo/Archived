<?php
	session_start();
	date_default_timezone_set('America/Sao_Paulo');
	require('vendor/autoload.php');
	
	define('INCLUDE_PATH_STATIC', 'http://192.168.122.250/web_php/classes/Views/pages/');
	define('INCLUDE_PATH', 'http://192.168.122.250/web_php/');
	
	$app = new classes\Application();

	$app->run();
?>
