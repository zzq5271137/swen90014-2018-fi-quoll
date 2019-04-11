<?php

	$mysqli = new mysqli('localhost', 'root', 'Ntfsfat32hfs+', 'unimelb');
	
	$json = file_get_contents('php://input');
	
	$obj = json_decode($json,true);

	$userid = $obj['userid'];	

	$result= $mysqli->query("SELECT * FROM `userinfo` WHERE `userid`=$userid");
	$array = array();
	
	if ($result->num_rows > 0) {
		$row = $result->fetch_assoc();
		$array[] = $row;
		echo'{"ClassDetails":'.json_encode($array).'}';		
		}
		else
		{		
		echo json_encode('try again');
		}
		mysqli_close('$mysqli');	
?>
