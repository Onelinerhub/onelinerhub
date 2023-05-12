# How to check if a value is not in an array using PHP and MySQL?
// plain

To check if a value is not in an array using PHP and MySQL, you can use the `in_array()` function. This function takes two parameters, the value to search for and the array to search in. It returns `true` if the value is found in the array, and `false` if it is not.

## Example code

```
$array = array("apple", "banana", "orange");

if (!in_array("grapes", $array)) {
    echo "Grapes are not in the array";
}
```

## Output example

```
Grapes are not in the array
```

## Code explanation

- `$array`: This is the array that we are searching in.
- `in_array()`: This is the function that we are using to search for the value. It takes two parameters, the value to search for and the array to search in.
- `!`: This is the logical operator that is used to check if the value is not in the array.
- `echo`: This is the command used to output the result of the search.

## Helpful links
- [PHP in_array() Function](https://www.w3schools.com/php/func_array_in_array.asp)

onelinerhub: [How to check if a value is not in an array using PHP and MySQL?](https://onelinerhub.com/php-mysql/how-to-check-if-a-value-is-not-in-an-array-using-php-and-mysql)