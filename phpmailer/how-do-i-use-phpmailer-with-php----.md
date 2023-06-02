# How do I use PHPMailer with PHP 5.6?
// plain

Using PHPMailer with PHP 5.6 is very straightforward.

1. Install PHPMailer using Composer: `composer require phpmailer/phpmailer`
2. Create a new instance of PHPMailer:
```
<?php
require 'vendor/autoload.php';

$mail = new PHPMailer;
...
```
3. Configure the mailer settings, such as the SMTP server, port, authentication, and encryption:
```
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'user@example.com';
$mail->Password = 'secret';
$mail->SMTPSecure = 'tls';
$mail->Port = 587;
```
4. Set the recipient and sender information:
```
$mail->setFrom('sender@example.com', 'Sender Name');
$mail->addAddress('recipient@example.com', 'Recipient Name');
```
5. Set the subject and body of the message:
```
$mail->Subject = 'PHPMailer Test Subject';
$mail->Body    = 'This is a test message using PHPMailer.';
```
6. Finally, send the message using `$mail->send()`:
```
if(!$mail->send()) {
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

* [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
* [Composer Installation](https://getcomposer.org/doc/00-intro.md#installation-linux-unix-osx)

onelinerhub: [How do I use PHPMailer with PHP 5.6?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-with-php----)