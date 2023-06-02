# How do I use PHPMailer to send emails?
// plain

PHPMailer is a library used to send emails using PHP. To use it, first you need to include the library in your project and create a PHPMailer object.

```php
<?php
require 'PHPMailerAutoload.php';

$mail = new PHPMailer;
```

Then you need to configure the PHPMailer object with the necessary settings, such as the SMTP server, the sender's email address, and the recipient's email address.

```php
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'user@example.com';
$mail->Password = 'secret';
$mail->From = 'sender@example.com';
$mail->addAddress('recipient@example.com');
```

Next, you need to create the email message, setting the subject, body, and any attachments.

```php
$mail->Subject = 'Test email';
$mail->Body = 'This is a test email sent with PHPMailer.';
$mail->addAttachment('/path/to/attachment.zip');
```

Finally, you can send the email using the `send()` method.

```php
if (!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
```

## Output example

```
Message has been sent
```

## Helpful links
- [PHPMailer official website](https://github.com/PHPMailer/PHPMailer)
- [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial)

onelinerhub: [How do I use PHPMailer to send emails?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-send-emails-1685698606)