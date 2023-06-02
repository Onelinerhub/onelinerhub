# How do I install and use PHPMailer on Ubuntu?
// plain

1. First, install PHPMailer by running `sudo apt-get install php-pear` in the terminal.
2. Next, install the PHPMailer package using PEAR by running `sudo pecl install mail` in the terminal.
3. After that, enable the package by adding `extension=mail.so` to the `php.ini` file.
4. Then, create a file in your project directory, for example `sendmail.php` and add the following code:
```php
<?php
require 'vendor/autoload.php';

$mail = new PHPMailer;

$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'username@example.com';
$mail->Password = 'password';
$mail->SMTPSecure = 'tls';
$mail->Port = 587;

$mail->setFrom('from@example.com', 'Your Name');
$mail->addAddress('recipient@example.com', 'Recipient Name');

$mail->Subject = 'Test Email';
$mail->Body = 'This is a test email!';

if(!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
```
5. Finally, run the `sendmail.php` file in the terminal using `php sendmail.php`
6. If the message was sent successfully, you should see the output `Message has been sent`.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [How To Install and Use PHPMailer](https://www.cloudways.com/blog/install-and-use-phpmailer/)

onelinerhub: [How do I install and use PHPMailer on Ubuntu?](https://onelinerhub.com/phpmailer/how-do-i-install-and-use-phpmailer-on-ubuntu)