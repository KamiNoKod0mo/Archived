<?php
namespace classes\Controllers;

class RegistrarController{
	public function index(){
		
		if(isset($_POST['registrar'])){
			$username = $_POST['username'];
			$password = $_POST['password'];
			$email = $_POST['email'];

			if(\classes\Models\UsuariosModel::emailExists($email)){
					\classes\Utilidades::alerta('Este e-mail já existe no banco de dados!');
					\classes\Utilidades::redirect(INCLUDE_PATH.'registrar');
				}else{
					//Registrar usuário.
					$password = \classes\Bcrypt::hash($password);
					$registro = \classes\MySql::connect()->prepare("INSERT INTO usuario VALUES (null,?,?,?)");
					$registro->execute(array($username,$password,$email));

					\classes\Utilidades::alerta('Registrado com sucesso!');
					\classes\Utilidades::redirect(INCLUDE_PATH);
				}

		}

		\classes\Views\MainView::render('registrar');
	}
}

?>