# How do I manually install PHPMailer?
// plain

1. Download the latest version of PHPMailer from [here](https://github.com/PHPMailer/PHPMailer).
2. Extract the zip file and copy the `src` directory into your project.
3. Include the `autoload.php` file in your project:
```php
require 'src/PHPMailer/src/PHPMailerAutoload.php';
```
4. Create a new `PHPMailer` instance:
```php
$mail = new PHPMailer;
```
5. Configure the mailer settings as needed, for example:
```php
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'user@example.com';
$mail->Password = 'secret';
$mail->SMTPSecure = 'tls';
$mail->Port = 587;
```
6. Set the message details:
```php
$mail->setFrom('from@example.com', 'Sender');
$mail->addAddress('to@example.com', 'Recipient');
$mail->Subject = 'PHPMailer Test';
$mail->Body = 'This is a test message from PHPMailer.';
```
7. Send the message:
```php
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

onelinerhub: [How do I manually install PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-manually-install-phpmailer)