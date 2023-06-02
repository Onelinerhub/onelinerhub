# How do I use PHPMailer to configure SMTP secure authentication?
// plain

PHPMailer is a library used to send emails from PHP. It can be used to configure SMTP secure authentication using the following steps:

1. Include the PHPMailer library in your project:
```
require 'PHPMailerAutoload.php';
```

2. Create an instance of the PHPMailer class:
```
$mail = new PHPMailer;
```

3. Configure the SMTP authentication settings:
```
$mail->isSMTP();
$mail->SMTPAuth = true;
$mail->Host = 'smtp.example.com';
$mail->Username = 'username';
$mail->Password = 'password';
$mail->SMTPSecure = 'tls';
```

4. Set the SMTP port:
```
$mail->Port = 587;
```

5. Set the other mail parameters:
```
$mail->From = 'from@example.com';
$mail->FromName = 'Sender Name';
$mail->addAddress('to@example.com', 'Recipient Name');
$mail->Subject = 'Subject';
$mail->Body = 'Message body';
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
- [SMTP Authentication with PHPMailer](https://www.codeofaninja.com/2015/06/php-smtp-authentication-with-phpmailer.html)

onelinerhub: [How do I use PHPMailer to configure SMTP secure authentication?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-configure-smtp-secure-authentication)