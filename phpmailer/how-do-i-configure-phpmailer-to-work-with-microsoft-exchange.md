# How do I configure PHPMailer to work with Microsoft Exchange?
// plain

1. First, you need to install and configure PHPMailer. You can do this by running the following command:

```
composer require phpmailer/phpmailer
```

2. Then, you need to configure PHPMailer to work with Microsoft Exchange. You can do this by setting the following parameters:

- Host: The hostname of your Microsoft Exchange server.
- Username: The username of your Microsoft Exchange account.
- Password: The password of your Microsoft Exchange account.
- SMTPSecure: Set this to 'tls'.
- Port: Set this to 587.

3. Next, you need to set up the PHPMailer object with the above parameters. You can do this by using the following code:

```
$mail = new PHPMailer();
$mail->Host = 'hostname';
$mail->Username = 'username';
$mail->Password = 'password';
$mail->SMTPSecure = 'tls';
$mail->Port = 587;
```

4. Finally, you can send emails using PHPMailer with Microsoft Exchange. You can do this by using the following code:

```
$mail->addAddress('recipient@example.com', 'Recipient Name');
$mail->Subject = 'PHPMailer Test';
$mail->Body = 'This is a test message sent using PHPMailer with Microsoft Exchange.';
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

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [Configuring PHPMailer for Microsoft Exchange](https://www.sitepoint.com/configure-phpmailer-microsoft-exchange/)

onelinerhub: [How do I configure PHPMailer to work with Microsoft Exchange?](https://onelinerhub.com/phpmailer/how-do-i-configure-phpmailer-to-work-with-microsoft-exchange)