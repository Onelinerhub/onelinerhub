# Drop all Mysql tables in a specific database

```php
$mysqli = new mysqli('localhost', 'user', 'pass', 'dbname');
$mysqli->query('SET foreign_key_checks = 0');
if ($result = $mysqli->query("SHOW TABLES")) {
	while($row = $result->fetch_array(MYSQLI_NUM)) {
		$mysqli->query('DROP TABLE IF EXISTS '.$row[0]);
		echo $row[0] . "\n";
	}
}

$mysqli->query('SET foreign_key_checks = 1');
$mysqli->close();
```

- `mysqli` - Mysql driver for PHP
- `SET foreign_key_checks = 0` - disable key checks so we can drop tables one by one
- `SHOW TABLES` - list all tables
- `fetch_array(MYSQLI_NUM)` - fetch row as a numbered array
- `'DROP TABLE IF EXISTS '.$row[0]` - drops selected table
- `SET foreign_key_checks = 1` - enable key checks after all tables were deleted


