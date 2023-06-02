# How can I use PHPMailer in Yii 1?
// plain

PHPMailer is a library for sending emails from PHP applications. It can be used with Yii 1 by following these steps:

1. Download the PHPMailer library from [GitHub](https://github.com/PHPMailer/PHPMailer).

2. Extract the library to `protected/vendors/phpmailer/` in your Yii 1 application.

3. Add the PHPMailer library to your application's autoloader:

```php
Yii::import('application.vendors.phpmailer.*');
```

4. Create an instance of the PHPMailer class and set the necessary properties (e.g. `Host`, `Username`, `Password`):

```php
$mail = new PHPMailer();
$mail->Host = 'smtp.example.com';
$mail->Username = 'username';
$mail->Password = 'password';
```

5. Set the recipient and message properties:

```php
$mail->addAddress('recipient@example.com');
$mail->Subject = 'Test Email';
$mail->Body = 'This is a test email sent from Yii 1';
```

6. Send the email:

```php
if ($mail->send()) {
    echo 'Email sent successfully!';
} else {
    echo 'Error sending email: ' . $mail->ErrorInfo;
}
```

7. Optionally, you can add attachments to the email:

```php
$mail->addAttachment('/path/to/file.pdf');
```

## Helpful links

- [PHPMailer on GitHub](https://github.com/PHPMailer/PHPMailer)
- [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki)

onelinerhub: [How can I use PHPMailer in Yii 1?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-in-yii--)