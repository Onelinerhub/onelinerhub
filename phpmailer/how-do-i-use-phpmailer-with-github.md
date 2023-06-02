# How do I use PHPMailer with GitHub?
// plain

PHPMailer is a popular open source library used for sending emails from PHP code. It can be used with GitHub in a few simple steps.

1. Install PHPMailer with Composer:
```
composer require phpmailer/phpmailer
```

2. Include the autoloader in your script:
```
require 'vendor/autoload.php';
```

3. Create a new PHPMailer instance:
```
$mail = new PHPMailer;
```

4. Configure the SMTP settings:
```
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'user@example.com';
$mail->Password = 'secret';
```

5. Set the email content:
```
$mail->Subject = 'PHPMailer Test';
$mail->Body = 'This is a test message.';
$mail->addAddress('recipient@example.com');
```

6. Send the email:
```
$mail->send();
```

7. Check for errors:
```
if (!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
```

**Output**:
```
Message has been sent
```

For more information, please refer to the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer).

onelinerhub: [How do I use PHPMailer with GitHub?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-with-github)