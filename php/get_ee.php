<?php
$host_name = 'localhost:3306';
$user_name = 'orclsql';
$pass_word = 'tan5321';
$database_name = 'flux';
$conn = mysql_connect($host_name, $user_name, $pass_word) or die ('Error connecting to mysql');
mysql_select_db($database_name);
 
$return_arr = array();
 
/* If connection to database, run sql statement. */
if ($conn)
{
  
    $fetch = mysql_query("select id, first_name from consultant where first_name like '%" . mysql_real_escape_string($_GET['q']) . "%'". " order by 1 limit 20");
     
    /* Retrieve and store in array the results of the query.*/
    while ($row = mysql_fetch_array($fetch, MYSQL_ASSOC)) {
        $row_array['id'] = $row['id'];
        $row_array['name'] = $row['first_name'];
        
        array_push($return_arr,$row_array);
    }
}
 
/* Free connection resources. */
mysql_close($conn);
 
/* Toss back results as json encoded array. */
echo json_encode($return_arr);
?>
