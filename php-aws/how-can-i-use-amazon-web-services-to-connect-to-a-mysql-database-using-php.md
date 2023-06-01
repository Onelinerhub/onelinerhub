# How can I use Amazon Web Services to connect to a MySQL database using PHP?
// plain

To connect to a MySQL database using PHP and Amazon Web Services (AWS), you will need to use the AWS SDK for PHP. The SDK provides an API for connecting to the database.

The following example code demonstrates how to connect to a MySQL database using the AWS SDK for PHP:

```
<?php
$rds = new Aws\Rds\RdsClient([
    'region'  => 'us-east-1',
    'version' => 'latest'
]);

$result = $rds->describeDBInstances([
    'DBInstanceIdentifier' => 'my-db-instance'
]);

$endpoint = $result['DBInstances'][0]['Endpoint']['Address'];
echo $endpoint;

$link = mysqli_connect($endpoint,"user","password","dbname") or die("Error " . mysqli_error($link));

/* check connection */
if (mysqli_connect_errno()) {
    printf("Connect failed: %s\n", mysqli_connect_error());
    exit();
}

$query = "SELECT * from users";
$res = mysqli_query($link,$query);

if($res === FALSE) {
    die(mysqli_error());
}

while($row = mysqli_fetch_array($res, MYSQLI_ASSOC)) {
    echo "The ID is: " . $row['id'] . " and the Username is: " . $row['username'];
}

mysqli_close($link);
?>
```

The example code will output the endpoint of the database instance and then use the endpoint to connect to the database. It will then execute a query to retrieve data from the users table.

## Code explanation

- `$rds = new Aws\Rds\RdsClient([` - Initializes a new RdsClient object
- `$result = $rds->describeDBInstances([` - Retrieves information about the database instance
- `$endpoint = $result['DBInstances'][0]['Endpoint']['Address'];` - Stores the endpoint of the database instance
- `$link = mysqli_connect($endpoint,"user","password","dbname") or die("Error " . mysqli_error($link));` - Connects to the database using the endpoint
- `$query = "SELECT * from users";` - Specifies the query to execute
- `$res = mysqli_query($link,$query);` - Executes the query
- `while($row = mysqli_fetch_array($res, MYSQLI_ASSOC)) {` - Iterates over the results of the query
- `echo "The ID is: " . $row['id'] . " and the Username is: " . $row['username'];` - Outputs the data from the query
- `mysqli_close($link);` - Closes the connection to the database

## Helpful links
- [AWS SDK for PHP](https://aws.amazon.com/sdk-for-php/)
- [RDSClient](https://docs.aws.amazon.com/aws-sdk-php/v3/api/class-Aws.Rds.RdsClient.html)
- [MySQLi](https://www.php.net/manual/en/book.mysqli.php)

onelinerhub: [How can I use Amazon Web Services to connect to a MySQL database using PHP?](https://onelinerhub.com/php-aws/how-can-i-use-amazon-web-services-to-connect-to-a-mysql-database-using-php)