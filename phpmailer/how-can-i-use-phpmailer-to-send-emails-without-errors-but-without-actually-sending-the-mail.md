# How can I use PHPMailer to send emails without errors but without actually sending the mail?
// plain

PHPMailer can be used to send emails without actually sending the mail by using the `SMTPDebug` property. This property can be set to `2` which will enable verbose debug output without actually sending the email. An example of how to do this is shown below:

```php
<?php
require 'PHPMailerAutoload.php';

$mail = new PHPMailer;

$mail->SMTPDebug = 2; // Enable verbose debug output

$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'user@example.com';
$mail->Password = 'secret';
$mail->SMTPSecure = 'tls';

$mail->From = 'from@example.com';
$mail->FromName = 'Mailer';
$mail->addAddress('joe@example.net', 'Joe User');
$mail->addReplyTo('info@example.com', 'Information');

$mail->isHTML(true);
$mail->Subject = 'Here is the subject';
$mail->Body    = 'This is the HTML message body <b>in bold!</b>';

if(!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
```

When this code is executed, the output will be as follows:

```
SMTP -> FROM SERVER:220 smtp.example.com ESMTP
SMTP -> FROM SERVER: 250-smtp.example.com 250-PIPELINING 250-SIZE 10240000 250-VRFY 250-ETRN 250-STARTTLS 250-AUTH PLAIN LOGIN 250-AUTH=PLAIN LOGIN 250-ENHANCEDSTATUSCODES 250-8BITMIME 250 DSN
SMTP -> FROM SERVER:220 2.0.0 Ready to start TLS
SMTP -> FROM SERVER: 250-smtp.example.com 250-PIPELINING 250-SIZE 10240000 250-VRFY 250-ETRN 250-AUTH PLAIN LOGIN 250-AUTH=PLAIN LOGIN 250-ENHANCEDSTATUSCODES 250-8BITMIME 250 DSN
SMTP -> FROM SERVER:250 OK
SMTP -> FROM SERVER:250 Accepted
SMTP -> FROM SERVER:354 Enter message, ending with "." on a line by itself
SMTP -> FROM SERVER:250 OK
Message has been sent
``

The `SMTPDebug` property is used to enable verbose debug output without actually sending the mail. This property can be set to `2` which will enable verbose debug output. The output of this property will show the server responses for each command sent to the server.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)

onelinerhub: [How can I use PHPMailer to send emails without errors but without actually sending the mail?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-to-send-emails-without-errors-but-without-actually-sending-the-mail)