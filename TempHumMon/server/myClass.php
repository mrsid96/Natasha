<?php
require_once 'config.php';
class myClass
{
	public function check($day,$time,$temp,$hum)
	{
		$con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
		$res=mysqli_query($con,"insert into logger (day,time,temp,hum) values ('$temp','$hum')");
		$arr = array();
		if (mysqli_fetch_array($res)[0] == $pass)
			$arr=array('check' => 'True');
		else
			$arr=array('check' => 'False');
		mysqli_close($con);
		return $arr;		
	}
}
?>