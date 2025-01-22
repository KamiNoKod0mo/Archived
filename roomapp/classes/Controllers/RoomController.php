<?php
namespace classes\Controllers;
class RoomController{
	public function index(){
		
	if(isset($_POST['comp'])){
		$criador = $_POST['criador'];
		$roomName = $_POST['roomName'];

		if(\classes\Models\UsuariosModel::roomExists($roomName)){
			
		}else{
			$room = \classes\MySql::connect()->prepare("INSERT INTO sala VALUES (?,?,?)");
			$room->execute(array($criador,1,$roomName));
		}
		
	}
	if(isset($_POST['num'])){
		$roomName2 = $_POST['roomName2'];
		//echo $roomName2;
		\classes\Models\UsuariosModel::roomDel($roomName2);
	}
	\classes\Views\MainView::render('room');
	}
}
?>