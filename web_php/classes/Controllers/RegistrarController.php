<?php
	
	namespace classes\Controllers;

	class RegistrarController{


		public function index(){

			if(isset($_POST['registrar'])){
				$nome = $_POST['nome'];
				$email = $_POST['email'];
				$senha = $_POST['senha'];
				if(!filter_var($email,FILTER_VALIDATE_EMAIL)){
					\classes\Utilidades::alerta('E-mail Inválido.');
					\classes\Utilidades::redirect(INCLUDE_PATH.'registrar');
				}else if(strlen($senha) < 6){
					\classes\Utilidades::alerta('Sua senha é muito curta.');
					\classes\Utilidades::redirect(INCLUDE_PATH.'registrar');
				}else if(\classes\Models\UsuariosModel::emailExists($email)){
					\classes\Utilidades::alerta('Este e-mail já existe no banco de dados!');
					\classes\Utilidades::redirect(INCLUDE_PATH.'registrar');
				}else{
					//Registrar usuário.
					$senha = \classes\Bcrypt::hash($senha);
					$registro = \classes\MySql::connect()->prepare("INSERT INTO usuarios VALUES (null,?,?,?,null,null)");
					$registro->execute(array($nome,$email,$senha));

					\classes\Utilidades::alerta('Registrado com sucesso!');
					\classes\Utilidades::redirect(INCLUDE_PATH);
				}
				
			}
			\classes\Views\MainView::render('registrar');
			

		}

	}

?>