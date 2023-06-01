# How can I use PHP PDO to connect to an AWS RDS database?
// plain

To connect to an AWS RDS database using PHP PDO, you need to have the following information:

1. The name of the database host
2. The port number
3. The database name
4. The username
5. The password

Once you have these details, you can use the following code to connect to the database:

```php
<?php
$host = '<hostname>';
$port = '<port>';
$dbname = '<database name>';
$username = '<username>';
$password = '<password>';

$dbh = new PDO("mysql:host=$host;port=$port;dbname=$dbname", $username, $password);
```

After executing this code, you should see a `PDO` object that represents the connection to the database.

## Helpful links

- [PHP PDO Documentation](https://www.php.net/manual/en/book.pdo.php)
- [AWS RDS Documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html)

onelinerhub: [How can I use PHP PDO to connect to an AWS RDS database?](https://onelinerhub.com/php-aws/how-can-i-use-php-pdo-to-connect-to-an-aws-rds-database)