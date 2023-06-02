# How do I configure PHPMailer to send emails using Gmail?
// plain

**Configuring PHPMailer to send emails using Gmail**

1. Download and install PHPMailer:
```
composer require phpmailer/phpmailer
```
2. Create a new `PHPMailer` instance:
```php
$mail = new PHPMailer;
```
3. Configure the SMTP settings:
```php
$mail->isSMTP();
$mail->Host = 'smtp.gmail.com';
$mail->SMTPAuth = true;
$mail->Username = 'your_gmail_username';
$mail->Password = 'your_gmail_password';
$mail->SMTPSecure = 'tls';
$mail->Port = 587;
```
4. Set the sender and recipient email addresses:
```php
$mail->setFrom('sender@example.com', 'Sender Name');
$mail->addAddress('recipient@example.com', 'Recipient Name');
```
5. Set the email subject and body:
```php
$mail->Subject = 'Email Subject';
$mail->Body    = 'This is the HTML message body <b>in bold!</b>';
```
6. Send the email:
```php
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

For more information and detailed instructions, please refer to the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki/Using-Gmail-with-XOAUTH2).

onelinerhub: [How do I configure PHPMailer to send emails using Gmail?](https://onelinerhub.com/phpmailer/how-do-i-configure-phpmailer-to-send-emails-using-gmail)