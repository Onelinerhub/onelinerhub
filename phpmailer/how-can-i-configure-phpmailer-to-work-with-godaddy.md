# How can I configure PHPMailer to work with GoDaddy?
// plain

To configure PHPMailer to work with GoDaddy, you need to make sure you have the following:

1. A correctly configured SMTP server:
```
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'username';
$mail->Password = 'password';
```

2. The correct port for the SMTP server:
```
$mail->Port = 465;
```

3. The correct authentication type:
```
$mail->SMTPSecure = 'ssl';
```

4. The correct from address:
```
$mail->From = 'name@example.com';
```

Once you have all of these configured correctly, you can then use PHPMailer to send emails through GoDaddy.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [GoDaddy SMTP Settings](https://www.godaddy.com/help/configure-email-clients-using-smtp-852)

onelinerhub: [How can I configure PHPMailer to work with GoDaddy?](https://onelinerhub.com/phpmailer/how-can-i-configure-phpmailer-to-work-with-godaddy)