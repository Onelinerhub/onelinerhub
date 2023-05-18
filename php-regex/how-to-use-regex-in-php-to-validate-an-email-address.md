# How to use regex in PHP to validate an email address?
// plain

Using regular expressions (regex) in PHP to validate an email address is a common task. The following example code block will check if an email address is valid:

```
<?php
$email = "example@example.com";
if (preg_match("/^([a-zA-Z0-9])+([a-zA-Z0-9\._-])*@([a-zA-Z0-9_-])+([a-zA-Z0-9\._-]+)+$/", $email)) {
    echo "Valid email address";
} else {
    echo "Invalid email address";
}
```

## Output example

```
Valid email address
```

The code consists of the following parts:

1. `$email = "example@example.com";` - This is the email address to be validated.
2. `preg_match("/^([a-zA-Z0-9])+([a-zA-Z0-9\._-])*@([a-zA-Z0-9_-])+([a-zA-Z0-9\._-]+)+$/", $email)` - This is the regular expression used to validate the email address. It checks for the presence of an @ symbol, a period, and a valid domain name.
3. `echo "Valid email address";` - This is the output if the email address is valid.
4. `echo "Invalid email address";` - This is the output if the email address is invalid.

## Helpful links

- [PHP Regular Expression Functions](https://www.w3schools.com/php/php_ref_pcre.asp)
- [Regular Expression Syntax](https://www.regular-expressions.info/refquick.html)

onelinerhub: [How to use regex in PHP to validate an email address?](https://onelinerhub.com/php-regex/how-to-use-regex-in-php-to-validate-an-email-address)