# How can I use PHPMailer to send emails through Yandex?
// plain

PHPMailer is a library that can be used to send emails through Yandex. To use PHPMailer to send emails through Yandex, you need to do the following:

1. Install the PHPMailer library:
```
composer require phpmailer/phpmailer
```

2. Create a new instance of PHPMailer:
```php
$mail = new PHPMailer;
```

3. Configure the SMTP settings to use Yandex:
```php
$mail->isSMTP();
$mail->Host = 'smtp.yandex.com';
$mail->SMTPAuth = true;
$mail->Username = 'username@yandex.com';
$mail->Password = 'password';
$mail->SMTPSecure = 'ssl';
$mail->Port = 465;
```

4. Set the email address and name of the sender:
```php
$mail->setFrom('username@yandex.com', 'John Doe');
```

5. Set the email address and name of the recipient:
```php
$mail->addAddress('recipient@example.com', 'Jane Doe');
```

6. Set the subject and body of the message:
```php
$mail->Subject = 'Hello';
$mail->Body = 'This is a test message.';
```

7. Finally, send the email:
```php
if ($mail->send()) {
    echo 'Message sent!';
} else {
    echo 'Message could not be sent.';
}
```

## Output example

```
Message sent!
```

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/tree/master/docs)
- [Yandex SMTP Settings](https://yandex.com/support/mail/mail-clients.html#smtp)

onelinerhub: [How can I use PHPMailer to send emails through Yandex?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-to-send-emails-through-yandex)