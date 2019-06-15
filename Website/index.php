<?php session_start();?>

<html>
<body text="white" style="background-color:grey;">
<h1>mysocial</h1>
<a href="signin_page.php">Sign-up</a>
<a href="login_page.php">Log-in</a>

<?php
// Create connection
$con=mysqli_connect("localhost","root","471-my-root","mysocial");

// Check connection
if (mysqli_connect_errno($con))
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }

if(!isset($_SESSION['email'])) {
  $posts=mysqli_query($con,"SELECT * FROM POST");
  $id = rand(100 , 999);
  $_SESSION['id'] = $id;
  $_SESSION['name'] = "anon";
  echo "I love you Eena";
} else {
  echo "<br>". "Welcome, ". $_SESSION['name'];
  $email = $_SESSION['email'];
  $posts=mysqli_query($con,"SELECT * FROM POST, LOGGED_IN WHERE email = '$email'");
  //$posts=mysqli_query($con,"SELECT * FROM POST");
  echo $_SESSION['id']. "<br>";//. $_SESSION['password']. "<br>";
}



echo "<table border='22'>
<tr>
<th>Link</th>
<th>Caption</th>
<th>Comments</th>
</tr>";
// <th>Email_address</th>

while($row = mysqli_fetch_array($posts))
 {
 echo "<tr>";
 echo "<td>" . "<a href=" . $row['Link'] . ">view</a>" . "</td>";
 echo "<td>" . $row['Caption'] . "</td>";
 echo "<td>" . "<a href=comment.php?link=".$row['Link'].">comments</a>" . "</td>";
//  echo "<td>" . $row['Email_address'] . "</td>";
 echo "</tr>";
 }
echo "</table>";


mysqli_close($con);
?>

</body>
</html>