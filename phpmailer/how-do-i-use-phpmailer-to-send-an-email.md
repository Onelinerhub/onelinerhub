# How do I use PHPMailer to send an email?
// plain

PHPMailer is a popular library for sending emails from PHP. To use PHPMailer, you need to include the library in your PHP code.

```
require 'PHPMailerAutoload.php';
```

Then, you need to create an instance of the PHPMailer class and set some initial parameters.

```
$mail = new PHPMailer;
$mail->SMTPDebug = 3;
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'user@example.com';
$mail->Password = 'secret';
$mail->SMTPSecure = 'tls';
$mail->Port = 587;
```

Next, you need to set the sender and recipient information.

```
$mail->From = 'from@example.com';
$mail->FromName = 'Sender Name';
$mail->addAddress('recipient@example.com', 'Recipient Name');
```

Then, you need to set the subject and message body.

```
$mail->Subject = 'PHPMailer Message';
$mail->Body = 'This is a message sent with PHPMailer.';
```

Finally, you can send the email using the `send()` method.

```
if(!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
```

## Output example
 `Message has been sent`

Parts of the code explained:
- `require 'PHPMailerAutoload.php';` - This includes the PHPMailer library in your code.
- `$mail = new PHPMailer;` - This creates an instance of the PHPMailer class.
- `$mail->SMTPDebug = 3;` - This sets the debug level.
- `$mail->isSMTP();` - This sets the mailer to use SMTP.
- `$mail->Host = 'smtp.example.com';` - This sets the SMTP host.
- `$mail->SMTPAuth = true;` - This sets SMTP authentication.
- `$mail->Username = 'user@example.com';` - This sets the SMTP username.
- `$mail->Password = 'secret';` - This sets the SMTP password.
- `$mail->SMTPSecure = 'tls';` - This sets the encryption protocol.
- `$mail->Port = 587;` - This sets the SMTP port.
- `$mail->From = 'from@example.com';` - This sets the sender email address.
- `$mail->FromName = 'Sender Name';` - This sets the sender name.
- `$mail->addAddress('recipient@example.com', 'Recipient Name');` - This sets the recipient email address and name.
- `$mail->Subject = 'PHPMailer Message';` - This sets the email subject.
- `$mail->Body = 'This is a message sent with PHPMailer.';` - This sets the email body.
- `if(!$mail->send()) {` - This checks if the email was sent successfully.
- `$mail->ErrorInfo;` - This prints the error message if the email was not sent.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)

onelinerhub: [How do I use PHPMailer to send an email?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-send-an-email)