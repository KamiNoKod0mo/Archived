<?php
namespace classes\Controllers;

class HomeController{
	public function index(){
		if(isset($_GET['loggout'])){
			session_unset();
			session_destroy();

			\classes\Utilidades::redirect(INCLUDE_PATH);
		}


		if(isset($_SESSION['login'])){
			\classes\Views\MainView::render('home');
		}else{

			if(isset($_POST['login'])){
					$email = $_POST['email'];
					$password = $_POST['password'];

					$verifica = \classes\MySql::connect()->prepare("SELECT * FROM usuario WHERE email = ?");
					$verifica->execute(array($email));

					if($verifica->rowCount() == 0){
						//Não existe o usuário!
						\classes\Utilidades::alerta('Não existe nenhum usuário com este e-mail...');
						\classes\Utilidades::redirect(INCLUDE_PATH);
					}else{
						$dados = $verifica->fetch();
						$senhaBanco = $dados['senha'];

						if(\classes\Bcrypt::check($password,$senhaBanco)){
							//Usuário logado com sucesso

							$_SESSION['login'] = $dados['email'];
							$_SESSION['id'] = $dados['id'];
							$_SESSION['nome'] = explode(' ',$dados['nome'])[0];
							
							\classes\Utilidades::alerta('Logado com sucesso!');
							\classes\Utilidades::redirect(INCLUDE_PATH);
						}else{
							\classes\Utilidades::alerta('Senha incorreta....');
							\classes\Utilidades::redirect(INCLUDE_PATH);
						}
					}
			}

			\classes\Views\MainView::render('login');
		}

	}
}


?>