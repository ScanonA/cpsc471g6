<?php session_start();

echo "<html>
<body text='white' style='background-color:grey;'>
<h1>mysocial</h1>
<a href='create_thread.php'>CreateThread</a>
<form action = 'search_thread.php' method = 'post'>
  <input type = 'text' name = 'search' placeholder = 'Search For Threads'>
  <input type = 'submit' name = 'submit search'> </button>
</form>";
if(isset($_GET['command']) && $_GET['command'] == 'logout'){
  session_unset();
}
if(!isset($_SESSION['email'])) {
  echo "<a href='sign-up.php'>Sign-up </a>
        <a href='login_page.php'>Log-in</a>";
}
if(isset($_SESSION['email'])) {
  echo "<a href='index.php?command=logout&'>Log out</a>";
}

// Create connection
$con=mysqli_connect("localhost","root","471-my-root","mysocial");

// Check connection
if (mysqli_connect_errno($con))
  {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
  }

  ?>

  <form action="index.php" method="get">
     Caption: <input type="text" name="caption"><br>
     Link: <input type="text" name="link"><br>
     <input type="submit" value="Submit">
  </form>
  
  <?php
  if(isset($_GET['caption']) && isset($_GET['link']))
  {
    $my_link = $_GET['link'];
    if(isset($_SESSION['email'])) {
      mysqli_query($con,"INSERT INTO POST (Link, Caption, Email_address) VALUES('". $my_link."','". $_GET['caption'] ."','". $_SESSION['email'] ."')");
    } else {
      mysqli_query($con,"INSERT INTO POST (Link, Caption) VALUES('". $my_link."','". $_GET['caption'] ."')");
    }
    echo "Link: '". $my_link ."' submitted!";
  }

if(!isset($_SESSION['email'])) { // get posts here
  $posts=mysqli_query($con,"SELECT * FROM POST");
  $id = rand(100 , 999);
  $_SESSION['id'] = $id;
  $_SESSION['name'] = "anon";
  // echo "I love you Eena";
} else {
  echo "<br>". "Welcome, ". $_SESSION['name'];
  $email = $_SESSION['email'];
  $posts=mysqli_query($con,"SELECT SUBSCRIBES_TO.Name, POST.Caption, CONTAINS.Link 
                            FROM POST, SUBSCRIBES_TO, THREAD, CONTAINS 
                            WHERE SUBSCRIBES_TO.Email_address = '$email' AND SUBSCRIBES_TO.Name = CONTAINS.Name AND SUBSCRIBES_TO.NAME = THREAD.NAME AND CONTAINS.Link = POST.Link");
  //$posts=mysqli_query($con,"SELECT * FROM POST");
  //echo $_SESSION['id']. "<br>";//. $_SESSION['password']. "<br>";
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