# How do I use PHPMailer to send emails through Namecheap?
// plain

PHPMailer is an open source library for sending emails in PHP. To use PHPMailer to send emails through Namecheap, you will need to:

1. Install PHPMailer using Composer, the PHP package manager:
```
composer require phpmailer/phpmailer
```

2. Create a new PHPMailer instance with your Namecheap credentials:
```
$mail = new PHPMailer;
$mail->isSMTP();
$mail->Host = 'smtp.namecheap.com';
$mail->SMTPAuth = true;
$mail->Username = 'username';
$mail->Password = 'password';
$mail->SMTPSecure = 'tls';
$mail->Port = 587;
```

3. Set the sender and recipient addresses:
```
$mail->setFrom('from@example.com', 'John Doe');
$mail->addAddress('to@example.com', 'Jane Doe');
```

4. Set the subject and body of the email:
```
$mail->Subject = 'Hello';
$mail->Body = 'This is a test message.';
```

5. Send the email:
```
if (!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
```

6. Output:
```
Message has been sent
```

For more information, see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki) and the [Namecheap SMTP setup guide](https://www.namecheap.com/support/knowledgebase/article.aspx/947/38/how-do-i-set-up-smtp-for-my-domain).

onelinerhub: [How do I use PHPMailer to send emails through Namecheap?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-send-emails-through-namecheap)