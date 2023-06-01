# How can I use PHP to generate a fake email address?
// plain

Using PHP, it is possible to generate a fake email address. The following example code block will generate a randomly generated email address that is formatted like a valid email address (but does not actually exist):

```
<?php

$domain = array("gmail.com", "yahoo.com", "hotmail.com");
$name = substr(str_shuffle("abcdefghijklmnopqrstuvwxyz"), 0, 8);

$fake_email = $name . "@" . $domain[array_rand($domain)];

echo $fake_email;

// Output:
// uvxgfqmf@yahoo.com

?>
```

The code block above will generate a fake email address using the following parts:

- `$domain`: An array containing the domain names you want to use.
- `$name`: A randomly generated 8-character string using the `str_shuffle()` function.
- `$fake_email`: The concatenation of `$name` and a randomly chosen domain name from `$domain` using the `array_rand()` function.
- `echo`: Output the generated email address.

## Helpful links
- [str_shuffle()](http://php.net/manual/en/function.str-shuffle.php)
- [array_rand()](http://php.net/manual/en/function.array-rand.php)

onelinerhub: [How can I use PHP to generate a fake email address?](https://onelinerhub.com/php-faker/how-can-i-use-php-to-generate-a-fake-email-address)