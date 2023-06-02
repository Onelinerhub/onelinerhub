# How can I use PHPMailer to validate an email address?
// plain

PHPMailer is an open source library for sending emails using PHP. It can be used to validate an email address by sending a verification email to the address and then checking for a response. Here is an example of how to use PHPMailer to validate an email address:

```php
<?php
// Include PHPMailer library
require 'path/to/PHPMailer/src/PHPMailer.php';

// Create a new PHPMailer object
$mail = new PHPMailer;

// Set the recipient's email address
$mail->addAddress('recipient@example.com');

// Set the email body
$mail->Body = 'This is a test email to validate your email address.';

// Send the email
if ($mail->send()) {
    echo 'Message sent!';
} else {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
}
```

## Output example
 `Message sent!`

The code above does the following:
1. Includes the PHPMailer library.
2. Creates a new PHPMailer object.
3. Sets the recipient's email address.
4. Sets the email body.
5. Sends the email.
6. Checks for a response and prints a message.

## Helpful links
- [PHPMailer Homepage](https://github.com/PHPMailer/PHPMailer)
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)

onelinerhub: [How can I use PHPMailer to validate an email address?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-to-validate-an-email-address)