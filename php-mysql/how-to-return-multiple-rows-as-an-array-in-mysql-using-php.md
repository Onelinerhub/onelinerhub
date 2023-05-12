# How to return multiple rows as an array in MySQL using PHP?
// plain

You can return multiple rows as an array in MySQL using PHP by using the `mysqli_fetch_all()` function. This function takes a result set as an argument and returns an array of associative arrays.

## Example code

```
$result = mysqli_query($conn, "SELECT * FROM table");
$data = mysqli_fetch_all($result, MYSQLI_ASSOC);
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

- `mysqli_query($conn, "SELECT * FROM table")`: This line executes a query to select all data from the table.
- `mysqli_fetch_all($result, MYSQLI_ASSOC)`: This line takes the result set from the query and returns an array of associative arrays.

## Helpful links
- [mysqli_fetch_all()](https://www.php.net/manual/en/mysqli-result.fetch-all.php)

onelinerhub: [How to return multiple rows as an array in MySQL using PHP?](https://onelinerhub.com/php-mysql/how-to-return-multiple-rows-as-an-array-in-mysql-using-php)