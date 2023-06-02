# How do I use PHPMailer to send emails from my localhost?
// plain

PHPMailer is an open source library for sending emails from a localhost using PHP. To use PHPMailer to send emails from localhost, the following steps should be taken:

1. Include the PHPMailer library in the project:

```
require_once('path/to/PHPMailer/PHPMailerAutoload.php');
```

2. Create a new PHPMailer object:

```
$mail = new PHPMailer;
```

3. Set the necessary properties:

```
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'username';
$mail->Password = 'password';
$mail->SMTPSecure = 'tls';
$mail->Port = 587;
```

4. Set up the email message:

```
$mail->setFrom('from@example.com', 'Sender Name');
$mail->addAddress('recipient@example.com', 'Recipient Name');
$mail->Subject = 'Email Subject';
$mail->Body = 'Email body in HTML format';
```

5. Send the email:

```
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

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [PHPMailer Quickstart](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial)

onelinerhub: [How do I use PHPMailer to send emails from my localhost?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-send-emails-from-my-localhost)