# How to format a phone number using regex in PHP?
// plain

Using regex in PHP to format a phone number is a useful way to ensure that the phone number is in the correct format. The following example code block will format a phone number in the format of (xxx) xxx-xxxx:

```
$phone_number = "1234567890";
$formatted_phone_number = preg_replace("/([0-9]{3})([0-9]{3})([0-9]{4})/", "($1) $2-$3", $phone_number);
echo $formatted_phone_number;
```

The output of the example code will be:

```
(123) 456-7890
```

## Code explanation


- `$phone_number = "1234567890";`: This is the original phone number that will be formatted.
- `$formatted_phone_number = preg_replace("/([0-9]{3})([0-9]{3})([0-9]{4})/", "($1) $2-$3", $phone_number);`: This is the regex expression that will be used to format the phone number. The expression looks for 3 digits, followed by 3 digits, followed by 4 digits. The parentheses and hyphens are added to the expression to format the phone number.
- `echo $formatted_phone_number;`: This will output the formatted phone number.

## Helpful links

- [PHP Regex](https://www.php.net/manual/en/book.regex.php)
- [Regular Expressions Tutorial](https://www.regular-expressions.info/tutorial.html)

onelinerhub: [How to format a phone number using regex in PHP?](https://onelinerhub.com/php-regex/how-to-format-a-phone-number-using-regex-in-php)