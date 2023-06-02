# How can I use Jet PHP Mailer to send emails?
// plain

[Jet PHP Mailer](https://github.com/NagaPraveen/jet-php-mailer) is a lightweight library for sending emails using PHP. To use Jet PHP Mailer, you need to include the library in your project and set up a few configuration variables.

```php
<?php

// Include the library
require_once 'path/to/JetPHPMailer.php';

// Create a new instance of the JetPHPMailer class
$mail = new JetPHPMailer();

// Configure the mailer
$mail->From = 'from@example.com';
$mail->FromName = 'From Name';
$mail->addAddress('to@example.com', 'To Name');
$mail->Subject = 'Subject';
$mail->Body = 'Your message here';

// Send the email
$mail->send();

// Output result
echo $mail->ErrorInfo;
```

The code above will create a new instance of the JetPHPMailer class and configure the mailer with the `From` and `FromName` properties, the recipient's address and name, the subject, and the body of the message. Finally, the `send()` method is executed to send the email. The `ErrorInfo` property will contain any errors that may have occurred during the sending process.

For more information on Jet PHP Mailer, please refer to the [documentation](https://github.com/NagaPraveen/jet-php-mailer/wiki).

onelinerhub: [How can I use Jet PHP Mailer to send emails?](https://onelinerhub.com/phpmailer/how-can-i-use-jet-php-mailer-to-send-emails)