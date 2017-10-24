<?php
require_once 'config.php';
class myClass
{
	public function check($user,$pass)
	{
		$con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
		$res=mysqli_query($con,"select pass from users where user = '$user'");
		//echo "<script>alert('$res');</script>";
		$arr = array();
		//echo mysqli_fetch_array($res)[0];
		if (mysqli_fetch_array($res)[0] == $pass)
			$arr=array('check' => 'True');
		else
			$arr=array('check' => 'False');
		return $arr;		
	}

	public function switchChange($sid,$status)
	{
		$con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
		date_default_timezone_set('Asia/Kolkata');
		$dat = date('Y-m-d');
		$tme = date('g:i');
		if($status=='ON')
			$req=mysqli_query($con,"insert into logger (datel,sid,start) values ('$dat','$sid','$tme')");
		else
			$req=mysqli_query($con,"update logger set stop = '$tme' where sid='$sid' and datel='$dat' and stop IS NULL");

		$res=mysqli_query($con,"update switches set $sid = '$status'");
		$arr = array();
		if ($res && $req)
			$arr=array('check' => 'True');
		else
			$arr=array('check' => 'False');
		return $arr;		
	}

    public function updateUser($user, $name, $hob, $place, $cal)
    {
        $con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
        $res=mysqli_query($con,"update users set name='$name', hob='$hob', place='$place', cal='$cal' where user='$user'");
        $arr = array();
        if ($res)
            $arr=array('check' => 'True');
        else
            $arr=array('check' => 'False');
        return $arr;
    }

    public function listAllUsers()
    {
        $con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
        $res=mysqli_query($con,"select user from users");
        $arr = array();
        while($row = $res->fetch_assoc())
        {
                $arr[]= $row;
        }
        return $arr;
    }
    public function updatePass($user,$pass)
    {
        $con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
        $res=mysqli_query($con,"update users set pass='$pass' where user='$user'");
        $arr = array();
        if ($res)
            $arr=array('check' => 'True');
        else
            $arr=array('check' => 'False');
        return $arr;
    }

    public function user_show($user)
    {
        $con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
        $res=mysqli_query($con,"select name, hob, place, cal, pass from users where user='$user'");
        $data=mysqli_fetch_array($res);
        $arr = array();
        if ($res)
            $arr=array('check' => 'True','name'=>$data[0],'hob'=>$data[1],'place'=>$data[2],'cal'=>$data[3],'pass'=>$data[4]);
        else
            $arr=array('check' => 'False');
        return $arr;
    }

	public function register($user,$pass,$grp)
	{
		$con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
		$res=mysqli_query($con,"insert into users (user,pass,grp) values('$user','$pass','$grp')");
		$arr = array();
		if ($res)
			$arr=array('check' => 'True');
		else
			$arr=array('check' => 'False');
		return $arr;	
	}

	public function show()
    {
            $con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
            $res=mysqli_query($con,"select * from switches");
            $arr = array();
            while($row = $res->fetch_assoc())
            {
                    $arr= $row;
            }
            return $arr;
    }

    public function logDay($day)
    {
    	$con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
        $res=mysqli_query($con,"select * from logger where datel='$day'");
        $arr = array();
        while($row = $res->fetch_assoc())
        {
                $arr[]= $row;
        }
        return $arr;
    }

    public function add_schedule($sid,$day,$stime,$etime,$status)
    {
    	$con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
    	$res=mysqli_query($con,"update schedules set day='$day', stime='$stime', etime='$etime', chk='YES', status='$status' where sid='$sid'");
		$arr = array();
		if ($res)
			$arr=array('check' => 'True');
		else
			$arr=array('check' => 'False');
		return $arr;	
    }
    public function scheduleChange($serial)
    {
    	$check=['NO','YES'];
    	$con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
    	$res1=mysqli_query($con,"update schedules set chk='".$check[$serial[0]]."' where sid='lone'");
    	$res2=mysqli_query($con,"update schedules set chk='".$check[$serial[1]]."' where sid='fone'");
    	$res3=mysqli_query($con,"update schedules set chk='".$check[$serial[2]]."' where sid='ltwo'");
    	$res4=mysqli_query($con,"update schedules set chk='".$check[$serial[3]]."' where sid='ftwo'");
    	$res5=mysqli_query($con,"update schedules set chk='".$check[$serial[4]]."' where sid='pump'");
    	$arr = array();
		if ($res1 && $res2 && $res3 && $res4 && $res5)
			$arr=array('check' => 'True');
		else
			$arr=array('check' => 'False');
		return $arr;
    }

    public function show_schedules()
    {
    	$con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
        $res=mysqli_query($con,"select * from schedules");
        $arr = array();
        while($row = $res->fetch_assoc())
        {
                $arr[]= $row;
        }
        return $arr;
    }
    
    public function logDays($day1,$day2)
    {
    	$con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
        $res=mysqli_query($con,"select * from logger where datel between '$day1' and '$day2'");
        $arr = array();
        while($row = $res->fetch_assoc())
        {
                $arr[]= $row;
        }
        return $arr;
    }  

    public function addItem($user,$type,$name,$cal)
    {
        $con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
        $res=mysqli_query($con,"insert into foodies values ('$user','$type','$name','$cal')");
        $arr = array();
        if ($res)
            $arr=array('check' => 'True');
        else
            $arr=array('check' => 'False');
        return $arr;
    }

    public function showItem($user,$type)
    {
        $con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
        $res=mysqli_query($con,"select name,cal from foodies where user = '$user' and type = '$type'");
        $arr = array();
        while($row = $res->fetch_assoc())
        {
                $arr[]= $row;
        }
        return $arr;
    }

    public function showFoodDets($user)
    {
        $con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
        $res=mysqli_query($con,"select type,name,cal from foodies where user = '$user'");
        $arr = array();
        while($row = $res->fetch_assoc())
        {
                $arr[]= $row;
        }
        return $arr;
    }

    public function addFoodLog($user,$type,$item,$cal)
    {
        date_default_timezone_set('Asia/Kolkata');
        $tdate= date('Y-m-d');
        $ttime= date('g:i');
        $con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
        $res=mysqli_query($con,"insert into foodlog values('$user','$type','$item','$cal','$tdate','$ttime')");
        $arr = array();
        if ($res)
            $arr=array('check' => 'True');
        else
            $arr=array('check' => 'False');
        return $arr;
    }

    public function addPredicate($user,$predicate,$serial)
    {
        $con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
        $check=['OFF','ON'];
        $res=mysqli_query($con,"insert into predicates(user, predicate, lone, fone, ltwo, ftwo, pump) values('$user','$predicate','".$check[$serial[0]]."','".$check[$serial[1]]."','".$check[$serial[2]]."','".$check[$serial[3]]."','".$check[$serial[4]]."')");
        $arr = array();
        if ($res)
            $arr=array('check' => 'True');
        else
            $arr=array('check' => 'False');
        return $arr;
    }

    public function delPre($pid)
    {
        $con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
        $res=mysqli_query($con,"delete from predicates where pid = '$pid'");
        $arr = array();
        if ($res)
            $arr=array('check' => 'True');
        else
            $arr=array('check' => 'False');
        return $arr;
    }

    public function showPredicates($user)
    {
        $con=mysqli_connect(DB_HOST,DB_USER,DB_PASS,DB_NAME);
        $res=mysqli_query($con,"select pid,predicate,lone,fone,ltwo,ftwo,pump from predicates where user='$user'");
        $arr = array();
        while($row = $res->fetch_assoc())
        {
                $arr[]= $row;
        }
        return $arr;
    }
}
?>
