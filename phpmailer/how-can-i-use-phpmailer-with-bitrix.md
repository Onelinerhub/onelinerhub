# How can I use PHPMailer with Bitrix?
// plain

PHPMailer is a popular library for sending emails from PHP. It can be used with Bitrix, a popular CMS, by following a few steps.

First, the PHPMailer library must be added to the project. This can be done by downloading the library from [GitHub](https://github.com/PHPMailer/PHPMailer) and including the necessary files in the project.

Next, the necessary configuration must be set in the `/bitrix/php_interface/init.php` file. This includes setting the `SMTP` host, port, username, and password.

```php
$mail = new PHPMailer;
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->Port = 587;
$mail->SMTPSecure = 'tls';
$mail->SMTPAuth = true;
$mail->Username = "user@example.com";
$mail->Password = "password";
```

Finally, the email can be sent using the `send()` method.

```php
$mail->setFrom('user@example.com');
$mail->addAddress('recipient@example.com');
$mail->Subject = 'Test email';
$mail->Body = 'This is a test email sent using PHPMailer';

if (!$mail->send()) {
    echo "Error sending email: " . $mail->ErrorInfo;
} else {
    echo "Email sent successfully!";
}
```

## Output example
 `Email sent successfully!`

In summary, using PHPMailer with Bitrix requires downloading the library, configuring the `SMTP` settings, and sending the email using the `send()` method.

onelinerhub: [How can I use PHPMailer with Bitrix?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-with-bitrix)