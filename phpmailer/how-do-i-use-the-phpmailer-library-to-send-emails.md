# How do I use the PHPMailer library to send emails?
// plain

The PHPMailer library is a popular open source library for sending emails. To use the library, you will need to include the PHPMailer class file in your PHP code.

```php
require 'PHPMailer.php';
```

You will then need to create a new instance of the PHPMailer class.

```php
$mail = new PHPMailer;
```

You can then configure the mail object with various settings such as the sender address, recipient address, subject, and message.

```php
$mail->setFrom('sender@example.com', 'Sender Name');
$mail->addAddress('recipient@example.com', 'Recipient Name');
$mail->Subject = 'PHPMailer Test';
$mail->Body = 'This is a test message.';
```

Finally, you can send the message using the `send()` method.

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

For more information, see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer).

onelinerhub: [How do I use the PHPMailer library to send emails?](https://onelinerhub.com/phpmailer/how-do-i-use-the-phpmailer-library-to-send-emails)