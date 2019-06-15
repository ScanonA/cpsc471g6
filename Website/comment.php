<html>
<body text="white" style="background-color:grey;">
<h1>Comments</h1>
<a href="index.php">Login</a>

<?php
// Create connection
$con=mysqli_connect("localhost","root","471-my-root","mysocial");

// Check connection
if (mysqli_connect_errno($con))
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }
  $currentlink = $_GET["link"];
?>

<form action="comment.php?link=".$currentlink method="get">
   <input type='hidden' name='link' value='<?php echo "$currentlink";?>'/>
   Comment: <input type="text" name="comment"><br>
   <input type="submit" value="Submit">
</form>

<?php

if(isset($_GET['comment']))
{
  $placeholder_name = 'bungle';
  $placeholder_id = 789;
  $my_comment = $_GET["comment"];
  mysqli_query($con,"INSERT INTO COMMENT (CText, Name, ID, Link) VALUES('". $my_comment."','". $placeholder_name ."','". $placeholder_id ."','". $currentlink ."')");
   echo "Comment: '". $my_comment ."' submitted!";
}

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