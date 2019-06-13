<html>
<body>
<h1>mysocial</h1>
<a href="signin_page.php">Sign-in</a>

<?php
// Create connection
$con=mysqli_connect("localhost","root","471-my-root","mysocial");

// Check connection
if (mysqli_connect_errno($con))
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }

$posts=mysqli_query($con,"SELECT * FROM POST");

echo "<table border='1'>
<tr>
<th>Link</th>
<th>Caption</th>
<th>Email_address</th>
</tr>";
while($row = mysqli_fetch_array($posts))
 {
 echo "<tr>";
 echo "<td>" . $row['Link'] . "</td>";
 echo "<td>" . $row['Caption'] . "</td>";
 echo "<td>" . $row['Email_address'] . "</td>";
 echo "</tr>";
 }
echo "</table>";


mysqli_close($con);
?>

</body>
</html>