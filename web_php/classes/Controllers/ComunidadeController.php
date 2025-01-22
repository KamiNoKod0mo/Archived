<?php
	
	namespace classes\Controllers;

	class ComunidadeController{


		public function index(){
			if(isset($_SESSION['login'])){

				if(isset($_GET['solicitarAmizade'])){
					$idPara = (int) $_GET['solicitarAmizade'];
					if(\classes\Models\UsuariosModel::solicitarAmizade($idPara)){
						\classes\Utilidades::alerta('Amizade solicitada com sucesso!');
						\classes\Utilidades::redirect(INCLUDE_PATH.'comunidade');
					}else{
						\classes\Utilidades::alerta('Ocorreu um erro ao solicitar a amizade...');
						\classes\Utilidades::redirect(INCLUDE_PATH.'comunidade');
					}
				}

			\classes\Views\MainView::render('comunidade');
			}else{
				\classes\Utilidades::redirect(INCLUDE_PATH);
			}
			
		}

	}

?>