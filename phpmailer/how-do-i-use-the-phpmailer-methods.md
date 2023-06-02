# How do I use the PHPMailer methods?
// plain

PHPMailer is a library for sending emails from PHP. It can be used to send plain text emails, HTML emails, attachments, and more. To use PHPMailer, first you need to include the necessary files and create an instance of the PHPMailer class.

```php
require 'PHPMailer/PHPMailerAutoload.php';
$mail = new PHPMailer;
```

To send an email, you need to set the appropriate properties of the PHPMailer instance and then call the `send()` method. For example, to send a plain text email with an attachment:

```php
$mail->setFrom('from@example.com', 'Your Name');
$mail->addAddress('to@example.com', 'Recipient Name');
$mail->Subject = 'PHPMailer Test';
$mail->Body = 'This is a plain text email body.';
$mail->addAttachment('/path/to/file.pdf');

if (!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
```

The code above will output `Message has been sent` if the email is sent successfully.

The PHPMailer library also provides other methods for setting and changing the properties of the PHPMailer instance, such as `addAttachment()`, `addCC()`, `addReplyTo()`, `addAddress()`, `setFrom()`, and `setSubject()`. For more information, please refer to the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/tree/master/docs).

onelinerhub: [How do I use the PHPMailer methods?](https://onelinerhub.com/phpmailer/how-do-i-use-the-phpmailer-methods)