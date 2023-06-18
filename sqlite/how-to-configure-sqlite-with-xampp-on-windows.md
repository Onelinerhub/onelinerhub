# How to configure SQLite with XAMPP on Windows?
// plain

1. Install XAMPP from [Apache Friends](https://www.apachefriends.org/index.html) website.
2. Download SQLite from [SQLite Download Page](https://www.sqlite.org/download.html).
3. Extract the downloaded file in `C:\xampp\php\ext` directory.
4. Open `php.ini` file in `C:\xampp\php` directory and add the following line at the end of the file `extension=php_sqlite3.dll`
5. Restart XAMPP.
6. Test the installation by running the following code in `C:\xampp\htdocs`

```
<?php
$db = new SQLite3('test.db');
$db->exec('CREATE TABLE foo (bar STRING)');
$db->exec("INSERT INTO foo (bar) VALUES ('This is a test')");
$result = $db->query('SELECT bar FROM foo');
var_dump($result->fetchArray());
?>

```

## Output example

```
array(1) {
  [0]=>
  string(14) "This is a test"
}
```

7. Finally, you can access the SQLite database through the XAMPP server.

onelinerhub: [How to configure SQLite with XAMPP on Windows?](https://onelinerhub.com/sqlite/how-to-configure-sqlite-with-xampp-on-windows)