<?php
require_once 'myClass.php';
$db = new myClass();
if(isset($_GET["day"]) &&  $_GET["time"]) && $_GET["temp"]) && isset($_GET["hum"]))
{
	echo json_encode($db->addData($_GET["day"],$_GET["time"],$_GET["temp"],$_GET["hum"]));	
}

else {
	echo 'Not Allowed';
}
?>
