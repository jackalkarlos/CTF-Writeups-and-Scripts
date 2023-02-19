<?php
session_start();
$servername = "localhost";
$username = "root";
$dbname = "ctf_test";
$password = "";
// Create connection
$conn = new mysqli($servername, $username, $password,$dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

$session=mysqli_real_escape_string($conn,$_COOKIE['PHPSESSID']);
$ip=$_SERVER['REMOTE_ADDR'];




$conn->query("INSERT into misc (ip,phpsess)values('$ip','$session')");

if($conn->query("select Distinct ip from misc where phpsess='$session'")->num_rows >20)
{
    echo "Flag{here}";
}
else
{
    echo "Still Not 20 ip yet :D";
}


?>