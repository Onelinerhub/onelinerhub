# How to create pagination in MySQL using PHP?
// plain

Pagination in MySQL using PHP can be created by using the `LIMIT` clause in the `SELECT` statement. This clause takes two parameters, the first one is the offset and the second one is the number of records to be returned.

## Example code

```
$sql = "SELECT * FROM table_name LIMIT $offset, $records_per_page";
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

- `$sql`: This is the SQL query that will be used to retrieve the data from the database. It uses the `LIMIT` clause to specify the offset and the number of records to be returned.
- `$offset`: This is the offset of the records to be returned. It is used to specify the starting point of the records to be returned.
- `$records_per_page`: This is the number of records to be returned.
- `$result`: This is the result of the query. It is an array of records that were returned from the database.

## Helpful links
- [MySQL LIMIT Clause](https://www.w3schools.com/sql/sql_limit.asp)
- [PHP MySQLi](https://www.w3schools.com/php/php_mysql_intro.asp)

onelinerhub: [How to create pagination in MySQL using PHP?](https://onelinerhub.com/php-mysql/how-to-create-pagination-in-mysql-using-php)