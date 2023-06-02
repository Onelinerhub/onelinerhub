# How can I use PHPMailer to send bulk emails?
// plain

PHPMailer is a library for sending emails from PHP. To send bulk emails with PHPMailer, you can use a loop to iterate over an array of email addresses and send an email to each one. For example:

```
<?php
// Import PHPMailer classes into the global namespace
// These must be at the top of your script, not inside a function
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Load Composer's autoloader
require 'vendor/autoload.php';

// Create a new PHPMailer instance
$mail = new PHPMailer;

// Email addresses to send to
$emails = array('user1@example.com', 'user2@example.com', 'user3@example.com');

// Loop through each email address
foreach ($emails as $email) {
    // Set who the message is to be sent to
    $mail->addAddress($email);

    // Set the subject line
    $mail->Subject = 'This is a bulk email';

    // Set the body of the message
    $mail->Body = 'This is a message sent in bulk.';

    // Send the message
    $mail->send();
}
```

This code will send an email with the subject line "This is a bulk email" and body "This is a message sent in bulk." to each address in the `$emails` array.

## Code explanation


- `use PHPMailer\PHPMailer\PHPMailer;` & `use PHPMailer\PHPMailer\Exception;`: These lines import the PHPMailer classes into the global namespace.
- `require 'vendor/autoload.php';`: This line loads Composer's autoloader.
- `$mail = new PHPMailer;`: This line creates a new PHPMailer instance.
- `$emails = array('user1@example.com', 'user2@example.com', 'user3@example.com');`: This line creates an array of email addresses.
- `$mail->addAddress($email);`: This line sets the recipient of the email.
- `$mail->Subject = 'This is a bulk email';`: This line sets the subject line of the email.
- `$mail->Body = 'This is a message sent in bulk.';`: This line sets the body of the email.
- `$mail->send();`: This line sends the email.

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [PHPMailer GitHub Repository](https://github.com/PHPMailer/PHPMailer)

onelinerhub: [How can I use PHPMailer to send bulk emails?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-to-send-bulk-emails)