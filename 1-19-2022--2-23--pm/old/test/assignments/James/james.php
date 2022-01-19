<html>
    <head>
        <title>Aliens Abducted Me - Report an Abduction</title> 
    </head>
    <body>


<?php

echo "Thank you for submiting the form";
echo "You were abducted " . $_POST['whenithappened'];
echo " and were gone for " . $_POST['howlong'] . "<br>";
echo "Describe them: " . $_POST['aliendescription'] . "<br>";
echo "Was fang there? " . $_POST['fangspotted'];
echo "Your email address is " . $_POST['email'];

$msg = $name . ` was abducted ` . $when_it_happened .
` and was gone for ` . $how_long . `.` .
`Number of aliens: ` . $show_many .
`Alien description: ` . $alien_description .
`What the did: ` . $what_they_did .
`Fang spotted: ` . $fang_spotted .
`Other comments: ` . $other;


?>

    </body>
</html>

