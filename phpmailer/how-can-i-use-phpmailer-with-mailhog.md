# How can I use PHPMailer with MailHog?
// plain

PHPMailer is an open source library for sending emails from PHP. It can be used with MailHog, a testing mail server for developers, by making a few simple configuration changes.

To use PHPMailer with MailHog, you need to set the `SMTP` host to `localhost` and the `port` to `1025`. You can also set the `SMTPSecure` option to `tls` to enable encryption.

Below is an example of how to use PHPMailer with MailHog:

```
require 'PHPMailerAutoload.php';

$mail = new PHPMailer;
$mail->isSMTP();
$mail->Host = 'localhost';
$mail->Port = 1025;
$mail->SMTPSecure = 'tls';

$mail->From = 'from@example.com';
$mail->FromName = 'Example Sender';
$mail->addAddress('to@example.com', 'Example Recipient');

$mail->Subject = 'Test Email';
$mail->Body = 'This is a test email sent using PHPMailer with MailHog';

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

The above code does the following:

1. Includes the PHPMailer library
2. Sets the SMTP host to `localhost` and the port to `1025`
3. Sets the `SMTPSecure` option to `tls`
4. Sets the sender and recipient addresses
5. Sets the subject and body of the email
6. Sends the email
7. Outputs the result

## Helpful links

- [PHPMailer](https://github.com/PHPMailer/PHPMailer)
- [MailHog](https://github.com/mailhog/MailHog)

onelinerhub: [How can I use PHPMailer with MailHog?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-with-mailhog)