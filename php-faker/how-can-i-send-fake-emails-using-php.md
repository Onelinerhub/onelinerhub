# How can I send fake emails using PHP?
// plain

Sending fake emails using PHP is possible with the help of the [PHPMailer](https://github.com/PHPMailer/PHPMailer) library. This library allows you to create and send fake emails using PHP code.

The following example code shows how to send a fake email using PHPMailer:

```php
// Include the PHPMailer library
require_once('path/to/PHPMailer/PHPMailerAutoload.php');

// Create a new PHPMailer object
$mail = new PHPMailer;

// Set the sender address
$mail->setFrom('fake@example.com', 'Fake Sender');

// Set the recipient address
$mail->addAddress('recipient@example.com', 'Recipient Name');

// Set the subject
$mail->Subject = 'Fake Email';

// Set the message body
$mail->Body = 'This is a fake email sent using PHPMailer.';

// Send the fake email
if (!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent.';
}
```

## Output example


```
Message has been sent.
```

The code above does the following:

1. Includes the PHPMailer library.
2. Creates a new PHPMailer object.
3. Sets the sender address.
4. Sets the recipient address.
5. Sets the subject.
6. Sets the message body.
7. Sends the fake email.

For more information about sending fake emails using PHP, please refer to the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki).

onelinerhub: [How can I send fake emails using PHP?](https://onelinerhub.com/php-faker/how-can-i-send-fake-emails-using-php)