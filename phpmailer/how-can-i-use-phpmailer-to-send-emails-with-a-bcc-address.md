# How can I use PHPMailer to send emails with a BCC address?
// plain

PHPMailer is an open-source library for sending emails with PHP. To use PHPMailer to send emails with a BCC address, you need to include the PHPMailer library in your PHP script and create an instance of the PHPMailer class.

```php
// Include PHPMailer library
require_once 'PHPMailer/PHPMailerAutoload.php';

// Create instance of PHPMailer
$mail = new PHPMailer;

// Set BCC address
$mail->addBCC('bcc@example.com');
```

You can then add the other required details such as the sender, recipient, and subject, as well as the message body. Finally, you can send the email using the `send()` method.

```php
// Set sender, recipient, subject, and body
$mail->setFrom('from@example.com', 'From Name');
$mail->addAddress('to@example.com', 'To Name');
$mail->Subject = 'PHPMailer BCC Test';
$mail->Body = 'This is a test of PHPMailer BCC';

// Send email
if ($mail->send()) {
    echo "Email sent successfully";
}
else {
    echo "Error sending email: " . $mail->ErrorInfo;
}
```

## Output example


```
Email sent successfully
```

## Code explanation


- `require_once 'PHPMailer/PHPMailerAutoload.php';`: Include PHPMailer library.
- `$mail = new PHPMailer;`: Create instance of PHPMailer class.
- `$mail->addBCC('bcc@example.com');`: Set BCC address.
- `$mail->setFrom('from@example.com', 'From Name');`: Set sender address and name.
- `$mail->addAddress('to@example.com', 'To Name');`: Set recipient address and name.
- `$mail->Subject = 'PHPMailer BCC Test';`: Set email subject.
- `$mail->Body = 'This is a test of PHPMailer BCC';`: Set email body.
- `$mail->send()`: Send email.

## Helpful links

- [PHPMailer](https://github.com/PHPMailer/PHPMailer)
- [Sending Emails with PHPMailer](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial)

onelinerhub: [How can I use PHPMailer to send emails with a BCC address?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-to-send-emails-with-a-bcc-address)