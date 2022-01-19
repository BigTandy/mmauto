<html>
<head>
    <title>Aliens Abducted me - Report an Abduction</title>
</head>

<body>
 <h2>Aliens Abducted me - Report an Abduction</h2>
<?php 
$dbc = mysqli_connect('localhost', 'testing', 'Testing', 'kevin')
or die('Error connecting to the the database');

$first_name = $_POST['firstname'];
$last_name = $_POST['lastname'];
$what_did_they_do_to_you = $_POST['whattheydid'];
$when_it_happened =  $_POST['whenithappened'];
$how_long = $_POST['howlong'];
$how_many = $_POST['howmany'];
$alien_description = $_POST['aliendescription'];
$fang_spotted = $_POST['fangspotted'];
$email = $_POST['email'];
$other = $_POST['other'];

$query = "INSERT INTO alien_abduction (first_name, last_name, when_it_happened, how_long, how_many, alien_description, what_they_did, fang_spotted, other,email)" .  "VALUES ('$first_name','$last_name', '$when_it_happened', '$how_long', '$how_many', '$alien_description', '$what_did_they_do_to_you', '$fang_spotted', '$other', '$email')";
$result = mysqli_query($dbc, $query)
or die('Error querying the MySQL database.');
mysqli_close($dbc);

 echo 'Thanks for submitting the form '. $first_name. ' '. $last_name. '<br />';
 echo 'You were abducted ' . $when_it_happened;
 echo ' and were gone for ' . $how_long . '<br />';
 echo 'Describe them:' . $alien_description . '<br />';
 echo 'Was fang there? ' . $fang_spotted . '<br />';
 echo 'Your email address is ' . $email . '<br />';
 echo 'What did they do?: '. $what_did_they_do_to_you. '<br />';
 echo 'Other information: ' . $other. '<br />';
?>
</body>
</html>