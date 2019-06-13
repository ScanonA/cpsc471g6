
<?php

$name = $_POST["name"];
$id = $_POST["id"];

echo $name. "<br>". $id. "<br>";


// Create connection
$con=mysqli_connect("localhost","root","471-my-root","mysocial");

// Check connection
if (mysqli_connect_errno($con))
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }
  
  $sql = "INSERT INTO USER (Name, ID) VALUES ('". $name."','". $id ."')";
 
 if (!mysqli_query($con,$sql))
  {
  die('Error: ' . mysqli_error($con));
  }
  
echo "1 record added";

mysqli_close($con);
?>

