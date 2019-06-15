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
$currentlink = $_GET["link"];
$comments=mysqli_query($con,"SELECT * FROM `comment` WHERE `Link` = '".$currentlink."'");

echo "<table border='22'>
<tr>
<th>Comment</th>
<th>Name</th>
<th>ID</th>
</tr>";
// <th>Email_address</th>

while($row = mysqli_fetch_array($comments))
 {
 echo "<tr>";
 echo "<td>" . $row['CText'] . "</td>";
 echo "<td>" . $row['Name'] . "</td>";
 echo "<td>" . $row['ID'] . "</td>";
 echo "</tr>";
 }
echo "</table>";

mysqli_close($con);
?>

</body>
</html>