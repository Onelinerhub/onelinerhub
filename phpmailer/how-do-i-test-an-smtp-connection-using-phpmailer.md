# How do I test an SMTP connection using PHPMailer?
// plain

Testing an SMTP connection using PHPMailer is a straightforward process. Below is an example code block to accomplish this:

```php
require 'PHPMailerAutoload.php';

$mail = new PHPMailer;

//Enable SMTP debugging
// 0 = off (for production use)
// 1 = client messages
// 2 = client and server messages
$mail->SMTPDebug = 2;

//Set the hostname of the mail server
$mail->Host = 'smtp.example.com';
//Set the SMTP port number - likely to be 25, 465 or 587
$mail->Port = 25;

//Whether to use SMTP authentication
$mail->SMTPAuth = true;
//Username to use for SMTP authentication
$mail->Username = "user@example.com";
//Password to use for SMTP authentication
$mail->Password = "secret";

//Set who the message is to be sent from
$mail->setFrom('from@example.com', 'First Last');

//Set an alternative reply-to address
$mail->addReplyTo('replyto@example.com', 'First Last');

//Set who the message is to be sent to
$mail->addAddress('whoto@example.com', 'John Doe');

//Set the subject line
$mail->Subject = 'PHPMailer SMTP test';

//Read an HTML message body from an external file, convert referenced images to embedded,
//convert HTML into a basic plain-text alternative body
$mail->msgHTML(file_get_contents('contents.html'), dirname(__FILE__));

//Replace the plain text body with one created manually
$mail->AltBody = 'This is a plain-text message body';

//send the message, check for errors
if (!$mail->send()) {
    echo "Mailer Error: " . $mail->ErrorInfo;
} else {
    echo "Message sent!";
}
```

This code will attempt to connect to the SMTP server specified in `$mail->Host`. The SMTP debug level is set to `2` which will print out client and server messages which can be useful for troubleshooting. The authentication settings are then set with `$mail->SMTPAuth`, `$mail->Username`, and `$mail->Password`. Finally, the message details are set with `$mail->setFrom()`, `$mail->addReplyTo()`, `$mail->addAddress()`, `$mail->Subject`, `$mail->msgHTML()`, and `$mail->AltBody`. The code will then attempt to send the message and print out either a success message or an error message.

Parts of the code:

- `$mail->SMTPDebug`: Sets the SMTP debug level.
- `$mail->Host`: Sets the hostname of the SMTP server.
- `$mail->Port`: Sets the SMTP port number.
- `$mail->SMTPAuth`: Whether to use SMTP authentication.
- `$mail->Username`: Username to use for SMTP authentication.
- `$mail->Password`: Password to use for SMTP authentication.
- `$mail->setFrom()`: Sets who the message is to be sent from.
- `$mail->addReplyTo()`: Sets an alternative reply-to address.
- `$mail->addAddress()`: Sets who the message is to be sent to.
- `$mail->Subject`: Sets the subject line.
- `$mail->msgHTML()`: Reads an HTML message body from an external file.
- `$mail->AltBody`: Sets a plain-text alternative body.
- `$mail->send()`: Sends the message and checks for errors.

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)
- [SMTP Debugging](https://github.com/PHPMailer/PHPMailer/wiki/SMTP-Debugging)

onelinerhub: [How do I test an SMTP connection using PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-test-an-smtp-connection-using-phpmailer)