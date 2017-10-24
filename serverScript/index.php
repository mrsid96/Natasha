<?php
require_once 'myClass.php';
$db = new myClass();

if(isset($_GET["user"]) && isset($_GET["name"]) && isset($_GET["hob"]) && isset($_GET["place"]) && isset($_GET["cal"]) )
{
	#update user details
	echo json_encode($db->updateUser($_GET["user"],$_GET["name"],$_GET["hob"],$_GET["place"],$_GET["cal"]));
}
else if(isset($_GET["user"]) && isset($_GET["pass"]) && isset($_GET["grp"]))
{
	#Admin Add new User
	echo json_encode($db->register($_GET["user"],$_GET["pass"],$_GET["grp"]));	
}
else if(isset($_GET["user"]) && isset($_GET["pass"]))
{
	#Check Login Page
	echo json_encode($db->check($_GET["user"],$_GET["pass"]));	
}
else if(isset($_GET["user"]) && isset($_GET["npass"]))
{
	#For password update
	echo json_encode($db->updatePass($_GET["user"],$_GET["npass"]));	
}
else if(isset($_GET["user"]) && isset($_GET["predicate"]) && isset($_GET["serial"]))
{
	#adding a new predicate for defined user.
	echo json_encode($db->addPredicate($_GET["user"],$_GET["predicate"],$_GET["serial"]));
}
else if(isset($_GET["user"]) && isset($_GET["showPredicate"]))
{
	#Show the list of predicates for a particular user.
	echo json_encode($db->showPredicates($_GET["user"]));
}
else if(isset($_GET["user"]) && isset($_GET["type"]) && isset($_GET["name"]) && isset($_GET["cal"]))
{
	#Add food types and preferences to the db
	echo json_encode($db->addItem($_GET["user"],$_GET["type"],$_GET["name"],$_GET["cal"]));
}
else if(isset($_GET["user"]) && isset($_GET["type"]))
{
	#Display the list of food under the type for the user.
	echo json_encode($db->showItem($_GET["user"],$_GET["type"]));
}
else if(isset($_GET["userFoodDet"]))
{
	#Display the list of all the food items along with the type for the food.
	echo json_encode($db->showFoodDets($_GET["userFoodDet"]));
}
else if(isset($_GET["user"]) && isset($_GET["FoodType"]) && isset($_GET["FoodItem"]) && isset($_GET["FoodCal"]))
{
	#Add individual food item to the type category.
	echo json_encode($db->addFoodLog($_GET["user"],$_GET["FoodType"],$_GET["FoodItem"],$_GET["FoodCal"]));
}
else if(isset($_GET["delPre"]))
{
	echo json_encode($db->delPre($_GET["delPre"]));
}
else if(isset($_GET["listusers"]))
{
	#Display the details of user
	echo json_encode($db->listAllUsers());
}
else if(isset($_GET["user"]))
{
	#Display the details of user
	echo json_encode($db->user_show($_GET["user"]));
}
else if(isset($_GET["sid"]) && isset($_GET["day"]) && isset($_GET["stime"]) && isset($_GET["etime"]) && isset($_GET["status"]))
{
	#Add the schedule to the db
	echo json_encode($db->add_schedule($_GET["sid"],$_GET["day"],$_GET["stime"],$_GET["etime"],$_GET["status"]));
}
else if(isset($_GET["sid"]) && isset($_GET["status"]))
{
	#Change the switch status
	echo json_encode($db->switchChange($_GET["sid"],$_GET["status"]));	
}
else if(isset($_GET["status"]))
{
	#Display all the status of the switches
	echo json_encode($db->show());
}
else if(isset($_GET["serial"]))
{
	#Toggle On/Off Scheduling
	echo json_encode($db->scheduleChange($_GET["serial"]));	
}
else if(isset($_GET["schedules"]))
{
	#Display all the schedules
	echo json_encode($db->show_schedules());
}
else if(isset($_GET["date1"]) && isset($_GET["date2"]))
{
	#Show the power logger between date1 and date2
	echo json_encode($db->logDays($_GET["date1"],$_GET["date2"]));
}
else if(isset($_GET["date1"]))
{
	#Show the power log for a single day
	echo json_encode($db->logDay($_GET["date1"]));
}
else 
{
	echo "NATASHA - AI Powered Smart Home Automation API Server.";	
}
?>
