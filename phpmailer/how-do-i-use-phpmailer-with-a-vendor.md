# How do I use PHPMailer with a vendor?
// plain

PHPMailer is a library used to send emails from PHP. It can be used with a vendor to send out emails on behalf of the vendor. Here is an example of how to use PHPMailer with a vendor:

```
<?php
// Import PHPMailer classes into the global namespace
// These must be at the top of your script, not inside a function
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Load Composer's autoloader
require 'vendor/autoload.php';

// Instantiate a new PHPMailer
$mail = new PHPMailer();

// Set up the mail server
$mail->Host = 'smtp.example.com';
$mail->Port = 587;
$mail->SMTPSecure = 'tls';
$mail->SMTPAuth = true;
$mail->Username = 'username@example.com';
$mail->Password = 'password';

// Set up the message
$mail->setFrom('username@example.com', 'Vendor Name');
$mail->addAddress('recipient@example.com');
$mail->Subject = 'Email from Vendor';
$mail->Body = 'This is an email from the vendor.';

// Send the message
$mail->send();

echo 'Message sent successfully!';
```

## Output example


`Message sent successfully!`

The code consists of the following parts:

1. `use PHPMailer\PHPMailer\PHPMailer;` and `use PHPMailer\PHPMailer\Exception;` - These two lines import the PHPMailer classes into the global namespace.
2. `require 'vendor/autoload.php';` - This line loads the Composer autoloader which is used to load the PHPMailer library.
3. `$mail = new PHPMailer();` - This line instantiates a new PHPMailer instance.
4. `$mail->Host = 'smtp.example.com';` - This line sets up the mail server.
5. `$mail->setFrom('username@example.com', 'Vendor Name');` - This line sets up the sender of the message.
6. `$mail->addAddress('recipient@example.com');` - This line adds the recipient of the message.
7. `$mail->Subject = 'Email from Vendor';` - This line sets the subject of the message.
8. `$mail->Body = 'This is an email from the vendor.';` - This line sets the body of the message.
9. `$mail->send();` - This line sends the message.

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)

onelinerhub: [How do I use PHPMailer with a vendor?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-with-a-vendor)