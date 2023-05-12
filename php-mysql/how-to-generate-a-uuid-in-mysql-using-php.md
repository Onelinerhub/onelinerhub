# How to generate a UUID in MySQL using PHP?
// plain

Generating a UUID in MySQL using PHP is a simple process. The following example code will generate a UUID and store it in a variable:
```
$uuid = uniqid('', true);
```
The output of this code will be a unique string of characters, such as `5f3d7f9f9f9f9f9f9f9f9f9f9f9f9f9f`.

The code consists of two parts:
1. `uniqid()`: This is a PHP function that generates a unique ID based on the current time in microseconds.
2. `true`: This is an optional parameter that tells the `uniqid()` function to generate a more random ID.

## Helpful links
- [PHP uniqid() Function](https://www.w3schools.com/php/func_misc_uniqid.asp)

onelinerhub: [How to generate a UUID in MySQL using PHP?](https://onelinerhub.com/php-mysql/how-to-generate-a-uuid-in-mysql-using-php)