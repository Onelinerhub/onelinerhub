# How to use a MySQL union in PHP?
// plain

MySQL UNION is a powerful operator used to combine the result sets of two or more SELECT statements into a single result set. It can be used in PHP to retrieve data from multiple tables in a single query.

## Example code

```
$sql = "SELECT * FROM table1
        UNION
        SELECT * FROM table2";
$result = mysqli_query($conn, $sql);
```

## Output example

```
Array
(
    [0] => Array
        (
            [id] => 1
            [name] => John
            [age] => 25
        )

    [1] => Array
        (
            [id] => 2
            [name] => Jane
            [age] => 30
        )

)
```

## Code explanation


1. `$sql`: This is the SQL query that contains the UNION operator.
2. `mysqli_query($conn, $sql)`: This is the function used to execute the query. `$conn` is the connection to the MySQL database.
3. `UNION`: This is the operator used to combine the result sets of two or more SELECT statements into a single result set.
4. `SELECT * FROM table1`: This is the first SELECT statement used to retrieve data from the first table.
5. `SELECT * FROM table2`: This is the second SELECT statement used to retrieve data from the second table.

## Helpful links

1. [MySQL UNION Operator](https://www.w3schools.com/sql/sql_union.asp)
2. [MySQLi Query](https://www.php.net/manual/en/mysqli.query.php)

onelinerhub: [How to use a MySQL union in PHP?](https://onelinerhub.com/php-mysql/how-to-use-a-mysql-union-in-php)