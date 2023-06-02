# How do I use PHPMailer to send an email with an attachment?
// plain

Using [PHPMailer](https://github.com/PHPMailer/PHPMailer) to send an email with an attachment is a fairly straightforward process.

First, include the PHPMailer library:
```php
require 'PHPMailerAutoload.php';
```

Then, create an instance of the PHPMailer class and set the necessary options:
```php
$mail = new PHPMailer;
$mail->setFrom('from@example.com', 'Your Name');
$mail->addAddress('to@example.com', 'Recipient Name');
$mail->Subject = 'PHPMailer Attachment';
$mail->Body = 'This is an automated message.';
```

Next, add the attachment to the message:
```php
$mail->addAttachment('/path/to/file.pdf');
```

Finally, send the message and check for errors:
```php
if (!$mail->send()) {
    echo "Mailer Error: " . $mail->ErrorInfo;
} else {
    echo "Message sent!";
}
```

## Output example

```
Message sent!
```

## Code explanation

1. `require 'PHPMailerAutoload.php'`: This line includes the PHPMailer library.
2. `$mail = new PHPMailer;`: This line creates an instance of the PHPMailer class.
3. `$mail->setFrom('from@example.com', 'Your Name');`: This sets the sender's address and name.
4. `$mail->addAddress('to@example.com', 'Recipient Name');`: This sets the recipient's address and name.
5. `$mail->Subject = 'PHPMailer Attachment';`: This sets the subject of the email.
6. `$mail->Body = 'This is an automated message.';`: This sets the body of the email.
7. `$mail->addAttachment('/path/to/file.pdf');`: This adds an attachment to the message.
8. `if (!$mail->send()) {`: This checks if the message was sent successfully.
9. `echo "Mailer Error: " . $mail->ErrorInfo;`: This prints the error message if an error occurred.
10. `echo "Message sent!";`: This prints a success message if the message was sent successfully.

## Helpful links
- [PHPMailer GitHub Repo](https://github.com/PHPMailer/PHPMailer)
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)

onelinerhub: [How do I use PHPMailer to send an email with an attachment?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-send-an-email-with-an-attachment)