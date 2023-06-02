# How do I use PHPMailer to send an email?
// plain

PHPMailer is a popular open source library for sending emails using PHP. It is easy to use and well documented.

To use PHPMailer, first you need to include the library in your project. You can download the library from [GitHub](https://github.com/PHPMailer/PHPMailer) or use [Composer](https://getcomposer.org/) to install it.

Then you need to create an instance of the `PHPMailer` class and set up the required parameters. For example:

```php
$mail = new PHPMailer();
$mail->IsSMTP();
$mail->Host = 'smtp.example.com';
$mail->Port = 587;
$mail->SMTPAuth = true;
$mail->Username = 'example@example.com';
$mail->Password = 'password';
```

Next you need to set up the message details. You can do this by setting the `From`, `To`, `Subject` and `Body` properties of the `PHPMailer` instance. For example:

```php
$mail->From = 'example@example.com';
$mail->FromName = 'Example Name';
$mail->AddAddress('recipient@example.com');
$mail->Subject = 'This is a test email';
$mail->Body = 'This is a test email sent using PHPMailer.';
```

Finally you need to call the `Send()` method of the `PHPMailer` instance to send the email. For example:

```php
if($mail->Send()) {
    echo 'Message sent successfully!';
} else {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
}
```

## Output example

```
Message sent successfully!
```

For more information, please refer to the [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki).

onelinerhub: [How do I use PHPMailer to send an email?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-send-an-email-1685704402)