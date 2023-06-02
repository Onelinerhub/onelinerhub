# How do I configure PHPmailer to use Zoho SMTP?
// plain

1. Install the latest version of PHPmailer using composer by running the command `composer require phpmailer/phpmailer`
2. Create a new instance of the PHPmailer class and set the SMTP host, username, and password for Zoho SMTP.
```php
$mail = new PHPMailer;
$mail->isSMTP();
$mail->Host = 'smtp.zoho.com';
$mail->SMTPAuth = true;
$mail->Username = 'username@zoho.com';
$mail->Password = 'password';
```
3. Set the SMTP port, encryption, and authentication type.
```php
$mail->Port = 587;
$mail->SMTPSecure = 'tls';
$mail->SMTPAuthType = 'LOGIN';
```
4. Set the sender and recipient information.
```php
$mail->setFrom('from@example.com', 'Mailer');
$mail->addAddress('to@example.com', 'User');
```
5. Set the subject and body of the message.
```php
$mail->Subject = 'Here is the subject';
$mail->Body    = 'This is the HTML message body <b>in bold!</b>';
```
6. Send the message and check for errors.
```php
if(!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
```
7. Output: `Message has been sent`

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [Zoho SMTP Settings](https://www.zoho.com/mail/help/adminconsole/server-settings.html)

onelinerhub: [How do I configure PHPmailer to use Zoho SMTP?](https://onelinerhub.com/phpmailer/how-do-i-configure-phpmailer-to-use-zoho-smtp)