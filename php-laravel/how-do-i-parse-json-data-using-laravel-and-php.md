# How do I parse JSON data using Laravel and PHP?
// plain

Parsing JSON data using Laravel and PHP is quite easy. Here's an example of how to do it:

```
<?php
$json = '{"name":"John","age":30,"city":"New York"}';

$data = json_decode($json);

echo $data->name;
echo $data->age;
echo $data->city;

// Output:
John
30
New York
```

The code above uses the `json_decode()` function to parse the JSON data into an object. Then, we access the data by using the object's properties (`name`, `age`, and `city`).

The parts of the code above are as follows:
- `$json`: This is the JSON data that we'll be parsing.
- `$data`: This is the object that stores the parsed data from the `json_decode()` function.
- `echo $data->name;`: This is how we access the `name` property of the `$data` object.

For more information, please see the [PHP json_decode()](https://www.php.net/manual/en/function.json-decode.php) documentation.

onelinerhub: [How do I parse JSON data using Laravel and PHP?](https://onelinerhub.com/php-laravel/how-do-i-parse-json-data-using-laravel-and-php)