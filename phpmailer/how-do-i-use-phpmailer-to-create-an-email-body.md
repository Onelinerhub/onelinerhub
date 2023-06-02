# How do I use PHPMailer to create an email body?
// plain

PHPMailer is a library used to send emails from a web server. It can be used to create an email body in a few simple steps.

1. Include the PHPMailer library:
```php
require 'PHPMailerAutoload.php';
```

2. Create a new instance of PHPMailer:
```php
$mail = new PHPMailer;
```

3. Set the From, To, Subject, and Body of the message:
```php
$mail->From = 'from@example.com';
$mail->addAddress('to@example.com');
$mail->Subject = 'Subject of the email';
$mail->Body = 'This is the body of the email.';
```

4. Send the email:
```php
if (!$mail->send()) {
    echo "Mailer Error: " . $mail->ErrorInfo;
} else {
    echo "Message sent!";
}
```

## Output example

```
Message sent!
```

For more information, see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer).

onelinerhub: [How do I use PHPMailer to create an email body?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-create-an-email-body)