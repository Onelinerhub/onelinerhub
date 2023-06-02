# How can I send a UTF-8 encoded email using PHPMailer?
// plain

Sending a UTF-8 encoded email using PHPMailer is easy. First, you need to create a new instance of the PHPMailer class:

```
$mail = new PHPMailer;
```

Then, you need to set the encoding to UTF-8:

```
$mail->CharSet = 'UTF-8';
```

You can then set the other parameters, such as the sender and recipient address, subject and body of the email:

```
$mail->setFrom('sender@example.com', 'Sender Name');
$mail->addAddress('recipient@example.com', 'Recipient Name');
$mail->Subject = 'UTF-8 encoded email';
$mail->Body = 'This is a UTF-8 encoded email.';
```

Finally, you can send the email:

```
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

### Code parts explanation

* `$mail = new PHPMailer;` - creates a new instance of the PHPMailer class.
* `$mail->CharSet = 'UTF-8';` - sets the encoding to UTF-8.
* `$mail->setFrom('sender@example.com', 'Sender Name');` - sets the sender address and name.
* `$mail->addAddress('recipient@example.com', 'Recipient Name');` - sets the recipient address and name.
* `$mail->Subject = 'UTF-8 encoded email';` - sets the email subject.
* `$mail->Body = 'This is a UTF-8 encoded email.';` - sets the email body.
* `if(!$mail->send()) {` - checks if the email was sent successfully.
* `echo 'Message could not be sent.';` - prints an error message if the email was not sent.
* `echo 'Mailer Error: ' . $mail->ErrorInfo;` - prints the error message.
* `echo 'Message has been sent';` - prints a success message if the email was sent successfully.

### Relevant links

* [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial)

onelinerhub: [How can I send a UTF-8 encoded email using PHPMailer?](https://onelinerhub.com/phpmailer/how-can-i-send-a-utf---encoded-email-using-phpmailer)