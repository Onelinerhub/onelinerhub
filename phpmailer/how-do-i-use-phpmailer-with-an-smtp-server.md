# How do I use PHPMailer with an SMTP server?
// plain

Using PHPMailer with an SMTP server is a simple process.

1. Include the PHPMailer library in your project:
```
require 'PHPMailer/PHPMailerAutoload.php';
```

2. Create a new instance of the PHPMailer class:
```
$mail = new PHPMailer();
```

3. Configure the SMTP server details:
```
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'username';
$mail->Password = 'password';
$mail->SMTPSecure = 'tls';
$mail->Port = 587;
```

4. Set the sender and recipient details:
```
$mail->setFrom('sender@example.com', 'Sender Name');
$mail->addAddress('recipient@example.com', 'Recipient Name');
```

5. Set the email subject and body:
```
$mail->Subject = 'PHPMailer SMTP test';
$mail->Body = 'This is a test of PHPMailer using SMTP';
```

6. Send the email:
```
if(!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
```

7. Output:
```
Message has been sent
```

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [SMTP Configuration](https://github.com/PHPMailer/PHPMailer/wiki/SMTP-Configuration)

onelinerhub: [How do I use PHPMailer with an SMTP server?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-with-an-smtp-server)