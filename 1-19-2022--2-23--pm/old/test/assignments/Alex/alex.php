<html>
<head>
    <title>Aliens Abducted Me - Report an Abduction</title>
</head>
<body>
    <h2>Aliens Abducted Me - Report an Abduction</h2>

    <?php
        $first_name = $_POST['firstname'];
        $last_name = $_POST['lastname'];
        $when_it_happened = $_POST['whenithappened'];
        $how_long = $_POST['howlong'];
        $how_many = $_POST['howmany'];
        $alien_description = $_POST['aliendescription'];
        $what_they_did = $_POST['whattheydid'];
        $fang_spotted = $_POST['fangspotted'];
        $email = $_POST['email'];
        $other = $_POST['other'];
        $name = $first_name . ' ' . $last_name;

        echo 'Thanks for submitting the form.<br />';
        echo 'Your name is: ' . $name . '<br />';
        echo 'You were abducted ' . $when_it_happened;
        echo ' and were gone for ' . $how_long . '<br />';
        echo 'There were ' . $how_many . " of them" . "<br />";
        echo 'Describe them: ' . $alien_description . '<br />';
        echo 'What they did: ' . $what_they_did . '<br />';
        echo 'Was Fang there? ' . $fang_spotted . '<br />';
        echo 'Your email address is ' . $email . '<br />';
        echo 'Other things that you added: ' . $other;

        $subject = 'Aliens Abducted Me - Abduction Report;';
        $to = 'mmurray@minuteman.org';

        $msg = "$name was abducted $when_it_happened and was gone for $how_long.\n" . 
        "number of aliens: $how_many\n" . 
        "Alien description: $alien_description\n" . 
        "what they did: $what_they_did\n" . 
        "Fang spotted: $fang_spotted\n" . 
        "Other commens: $other";
        
    ?>

    <?php

    $dbc = mysqli_connect ('localhost', 'testing', 'Testing', 'alex')
    or die('Error connecting to MySQL Server.');

    $query = "INSERT INTO aliens_abduction (first_name, last_name, when_it_happened, how_long, how_many, alien_description, what_they_did, fang_spotted, other, email)
    
    VALUES ('$first_name', '$last_name', '$when_it_happened', '$how_long', '$how_many', '$alien_description', '$what_they_did', '$fang_spotted', '$other', '$email')";

    $result = mysqli_query($dbc, $query)
    or die ('Error Querying database.');

    mesqli_close ($dbc);

    ?>

</body>
</html>