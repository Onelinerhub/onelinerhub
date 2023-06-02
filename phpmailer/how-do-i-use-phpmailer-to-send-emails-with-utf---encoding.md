# How do I use PHPMailer to send emails with UTF-8 encoding?
// plain

PHPMailer is a popular open source library for sending emails using PHP. It supports various encodings including UTF-8, and can be used to send emails with UTF-8 encoding.

To use PHPMailer to send emails with UTF-8 encoding, first you need to include the PHPMailer library in your PHP script.

```php
require_once 'path/to/PHPMailer/PHPMailerAutoload.php';
```

Then create an instance of the PHPMailer class and set the encoding to UTF-8:

```php
$mail = new PHPMailer;
$mail->CharSet = 'UTF-8';
```

Next, set the other mail parameters such as the sender, recipient, subject and body.

```php
$mail->setFrom('sender@example.com', 'Sender Name');
$mail->addAddress('recipient@example.com', 'Recipient Name');
$mail->Subject = 'Email Subject';
$mail->Body = 'Email Body';
```

Finally, send the email using the `send()` method:

```php
if ($mail->send()) {
    echo 'Message sent!';
} else {
    echo 'Message not sent!';
}
```

## Output example

```
Message sent!
```

## Helpful links
- [PHPMailer](https://github.com/PHPMailer/PHPMailer)
- [PHPMailer wiki](https://github.com/PHPMailer/PHPMailer/wiki)

onelinerhub: [How do I use PHPMailer to send emails with UTF-8 encoding?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-send-emails-with-utf---encoding)