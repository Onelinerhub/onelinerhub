# How do I use PHPMailer with SSL?
// plain

PHPMailer is a popular open source library used for sending emails from PHP. To use PHPMailer with SSL, you first need to include the PHPMailer library in your project.

```
require 'PHPMailerAutoload.php';
```

Then, create a new instance of the PHPMailer class and set the necessary parameters for SSL.

```
$mail = new PHPMailer();
$mail->SMTPDebug = 2;
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'username';
$mail->Password = 'password';
$mail->SMTPSecure = 'ssl';
$mail->Port = 465;
```

Next, add the necessary information such as the recipient's email address, the subject of the email, and the message body.

```
$mail->addAddress('recipient@example.com');
$mail->Subject = 'Test Email using PHPMailer and SSL';
$mail->Body = 'This is a test email using PHPMailer and SSL.';
```

Finally, send the email using the `send()` method.

```
if ($mail->send()) {
    echo 'Message sent successfully!';
} else {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
}
```

## Output example
 `Message sent successfully!`

## Code explanation
**
- `require 'PHPMailerAutoload.php'` - This line includes the PHPMailer library in the project.
- `$mail = new PHPMailer()` - This line creates a new instance of the PHPMailer class.
- `$mail->SMTPDebug = 2` - This line sets the debug level to 2.
- `$mail->isSMTP()` - This line sets the mailer to use SMTP.
- `$mail->Host` - This line sets the SMTP host.
- `$mail->SMTPAuth` - This line sets SMTP authentication.
- `$mail->Username` - This line sets the SMTP username.
- `$mail->Password` - This line sets the SMTP password.
- `$mail->SMTPSecure` - This line sets the encryption protocol to SSL.
- `$mail->Port` - This line sets the SMTP port.
- `$mail->addAddress()` - This line adds the recipient's email address.
- `$mail->Subject` - This line sets the subject of the email.
- `$mail->Body` - This line sets the message body.
- `$mail->send()` - This line sends the email.

**## Helpful links**
- PHPMailer Documentation: https://github.com/PHPMailer/PHPMailer
- PHPMailer Tutorial: https://code.tutsplus.com/tutorials/how-to-use-phpmailer-to-send-emails-securely-in-php--cms-27177

onelinerhub: [How do I use PHPMailer with SSL?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-with-ssl)