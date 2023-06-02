# How can I use PHPMailer to validate email addresses?
// plain

PHPMailer is a library that can be used to validate email addresses. It provides a set of functions to validate the syntax of email addresses, check if the domain part of the address exists, and check if the email address can receive messages.

## Example code

```
<?php
// include the PHPMailer library
require 'PHPMailer/PHPMailerAutoload.php';

// create a new PHPMailer object
$mail = new PHPMailer();

// validate an email address
$valid = $mail->validateAddress('user@example.com');

if ($valid) {
    echo 'The email address is valid';
} else {
    echo 'The email address is not valid';
}
```

## Output example

```
The email address is valid
```

The code above uses the following parts:
- `require 'PHPMailer/PHPMailerAutoload.php'` - This line includes the PHPMailer library.
- `$mail = new PHPMailer()` - This line creates a new PHPMailer object.
- `$valid = $mail->validateAddress('user@example.com')` - This line validates the email address `user@example.com`.
- `if ($valid) {...} else {...}` - This block checks the result of the validation and prints a message.

For more information, see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer).

onelinerhub: [How can I use PHPMailer to validate email addresses?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-to-validate-email-addresses)