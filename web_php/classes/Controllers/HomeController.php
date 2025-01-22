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
				//Renderiza a home do usuário.

				//Existe pedido de amizade?

				if(isset($_GET['recusarAmizade'])){
					$idEnviou = (int) $_GET['recusarAmizade'];
					\classes\Models\UsuariosModel::atualizarPedidoAmizade($idEnviou,0);
					\classes\Utilidades::alerta('Amizade Recusada :(');
					\classes\Utilidades::redirect(INCLUDE_PATH);
				}else if(isset($_GET['aceitarAmizade'])){
					$idEnviou = (int) $_GET['aceitarAmizade'];
					if(\classes\Models\UsuariosModel::atualizarPedidoAmizade($idEnviou,1)){
					\classes\Utilidades::alerta('Amizade aceita!');
					\classes\Utilidades::redirect(INCLUDE_PATH);
					}else{
					\classes\Utilidades::alerta('Ops.. um erro ocorreu!');
					\classes\Utilidades::redirect(INCLUDE_PATH);
					}
				}

				//Existe postagem no feed?


				if(isset($_POST['post_feed'])){

					if($_POST['post_content'] == ''){
						\classes\Utilidades::alerta('Não permitimos posts vázios :(');
						\classes\Utilidades::redirect(INCLUDE_PATH);
					}

					\classes\Models\HomeModel::postFeed($_POST['post_content']);
					\classes\Utilidades::alerta('Post feito com sucesso!');
					\classes\Utilidades::redirect(INCLUDE_PATH);
				}
				


				\classes\Views\MainView::render('home');
			}else{
				//Renderizar para criar conta.

				if(isset($_POST['login'])){
					$login = $_POST['email'];
					$senha = $_POST['senha'];

					

					//Verificar no banco de dados.

					$verifica = \classes\MySql::connect()->prepare("SELECT * FROM usuarios WHERE email = ?");
					$verifica->execute(array($login));



					
					if($verifica->rowCount() == 0){
						//Não existe o usuário!
						\classes\Utilidades::alerta('Não existe nenhum usuário com este e-mail...');
						\classes\Utilidades::redirect(INCLUDE_PATH);
					}else{
						$dados = $verifica->fetch();
						$senhaBanco = $dados['senha'];
						if(\classes\Bcrypt::check($senha,$senhaBanco)){
							//Usuário logado com sucesso
							
							$_SESSION['login'] = $dados['email'];
							$_SESSION['id'] = $dados['id'];
							$_SESSION['nome'] = explode(' ',$dados['nome'])[0];
							$_SESSION['img'] = $dados['img'];
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