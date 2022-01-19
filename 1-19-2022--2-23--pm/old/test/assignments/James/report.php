<html>
<head>        
<title>Aliens Abducted Me - Report an Abduction</title>
</head>
<body>

<h2>Aliens Abducted Me - Report an Abduction</h2>
<?php

$first_name = $_POST['firstname'];
$last_name = $_POST['lastname'];
$email = $_POST['email'];
$when_it_happened = $_POST['whenithappened'];
$how_long = $_POST['howlong'];
$how_many = $_POST['howmany'];
$alien_description = $_POST['aliendescription'];
$what_they_did = $_POST['whattheydid'];
$fang_spotted = $_POST['fangspotted'];
$other = $_POST['other'];
$name = $first_name . $last_name;

echo 'Thanks for submitting the form '. $first_name . ' ' . $last_name . '<br />';
echo 'You were abducted  '. $when_it_happened;
echo ' and were gone for  ' . $how_long . '<br />';
echo 'How many did you see? ' . $how_many . '<br /';
echo 'Describe them: ' . $alien_description . '<br />';
echo 'What did they do to you? ' . $what_they_did . '<br /';
echo 'Was Fang there? ' . $fang_spotted . '<br />';
echo 'Your email address is ' . $email . '<br />';
echo 'Other: ' . $other;

$to = 'owen@aliensabductme.com';
$subject = 'Aliens Adubcted Me - Abduction Report';
$msg = $name . ' was abducted ' ;
$when_it_happened . ' and was gone for ' ;
$how_long . '.' . 'Number of aliens: ' ; 
$how_many . 'Alien description: ' ; 
$alien_description . 'What they did:' ; 
$what_they_did . 'Fang spotted:' ; 
$fang_spotted . 'Other comments: ' ; 
$other;

?>
<?php
$dbc = mysqli_connect('localhost', 'testing', 'Testing', 'james') or die('Error connecting to MySQL Server.');

$query = "INSERT INTO aliens_abduction (first_name, last_name, when_it_happened, how_long, how_many, alien_description, what_they_did, fang_spotted, other, email)".

"VALUES ('$first_name', '$last_name', '$when_it_happened', '$how_long', '$how_many', '$alien_description', '$what_they_did', '$fang_spotted', '$other', '$email')";

$result = mysqli_query($dbc, $query)
or die ('Error querying database.');

mysqli_close ($dbc);
?>
</body>
</html>