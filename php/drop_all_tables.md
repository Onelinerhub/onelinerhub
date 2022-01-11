# Drop all mysql tables in database

```php
$mysqli = new mysqli("localhost", "user", "pass", "dbname");
$mysqli->query(‘SET foreign_key_checks = 0’);
if ($result = $mysqli->query(“SHOW TABLES”)) {
	while($row = $result->fetch_array(MYSQLI_NUM)) {
		$mysqli->query(‘DROP TABLE IF EXISTS ‘.$row[0]);
		echo $row[0].”,\n”;
	}
}

$mysqli->query(‘SET foreign_key_checks = 1’);
$mysqli->close();
```

set your real database connection information
- localhost : database server name
- user : database username
- pass : database password
- dbname : database name