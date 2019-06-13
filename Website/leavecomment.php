<html>
<body text="white" style="background-color:grey;">
<h1>comment</h1>
<a href="index.php">Login</a>

<?php
// Create connection
$con=mysqli_connect("localhost","root","471-my-root","mysocial");

// Check connection
if (mysqli_connect_errno($con))
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }

// $posts=mysqli_query($con,"INSERT INTO COMMENT (CText, Name, ID, Link) VALUE(%s, %s, %s, %s)");




mysqli_close($con);
?>

</body>
</html>