<html>
    <head>
        <title>Abducted</title>
    </head>
    <body>


<?php

$host="localhost";
$user="testing";
$password="Testing";
$dbname="bud";

$con = new mysqli($host, $user, $password, $dbname)
	or die ('Could not connect to the database server' . mysqli_connect_error());

//$con->close();

$fname = $_POST['firstname'];
$lname = $_POST['lastname'];
$howmany = $_POST['howmany'];
$whatdone = $_POST['whattheydid'];
$other = $_POST['other'];
$when = $_POST['whenithappened'];
$howlong = $_POST['howlong'];
$discrip = $_POST['aliendescription'];
$fang = $_POST['fangspotted'];


echo "Thank you for submiting the form";
echo "You were abducted " . $_POST['whenithappened'];
echo " and were gone for " . $_POST['howlong'] . "<br>";
echo "Describe them: " . $_POST['aliendescription'] . "<br>";
echo "Was fang there? " . $_POST['fangspotted'];
echo "Your email address is " . $_POST['email'];

$msg = $fname . " " . $lname . " Was Abducted " . $_POST['whenithappened'] . " And was gone for " . $_POST['howlong'] . " #Aliens " . $howmany . " Discript: " . $_POST['aliendescription'] . " What they did " 
. $whatdone . " Fang Spotterd " . $_POST['fangspotted'] . " Other: " . $other;

$subject = "Aliens Abducted Me - Report";
$email = $_POST['email'];
$to = "mmurray@minuteman.org";



$result = mysqli_query($con, "INSERT INTO `bud`.`dog` (`id`, `firstname`, `lastname`, `howmany`, `whatdid`, `other`, `when`, `howlong`, `descip`, `fangspotted`, `email`) VALUES (NULL, '$fname', '$lname', '$howmany', '$whatdone', '$other', '$when', '$howlong', '$discrip', '$fang', '$email');");

echo $result;

mysqli_close($con);

#mail($to, $subject, $msg);


?>

    </body>
</html>
