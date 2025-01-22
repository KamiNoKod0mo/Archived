<?php
	
	namespace classes\Models;
	class UsuariosModel{
		public static function emailExists($email){
			$pdo = \classes\MySql::connect();
			$verificar = $pdo->prepare("SELECT email FROM usuario WHERE email = ?");
			$verificar->execute(array($email));

			if($verificar->rowCount() == 1){
				//Email existe.
				return true;
			}else{
				return false;
			}
		}

		public static function roomExists($hash){
			$pdo = \classes\MySql::connect();
			$verificar = $pdo->prepare("SELECT hash FROM sala WHERE hash = ?");
			$verificar->execute(array($hash));

			if($verificar->rowCount() == 1){
				
				return true;
			}else{
				return false;
			}
		}

		public static function roomDel($hash){
			$pdo = \classes\MySql::connect();
			$verificar = $pdo->prepare("DELETE FROM sala WHERE hash = ?");
			$verificar->execute(array($hash));

			\classes\Utilidades::redirect(INCLUDE_PATH);

		}
	}

?>