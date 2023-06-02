# How can I set up PHPMailer to use Zimbra SMTP?
// plain

To set up PHPMailer to use Zimbra SMTP, the following steps should be taken:

1. Install PHPMailer:
```
composer require phpmailer/phpmailer
```

2. Create a new instance of PHPMailer:
```
$mail = new PHPMailer;
```

3. Set the host and port of the Zimbra SMTP server:
```
$mail->Host = 'smtp.zimbra.com';
$mail->Port = 587;
```

4. Set the authentication type to use:
```
$mail->SMTPAuth = true;
```

5. Set the username and password to access the SMTP server:
```
$mail->Username = 'user@example.com';
$mail->Password = 'password';
```

6. Set the mailer type to use:
```
$mail->Mailer = 'smtp';
```

7. Finally, send the mail:
```
$mail->send();
```

## Code explanation
**

1. `composer require phpmailer/phpmailer` - This command will install PHPMailer.

2. `$mail = new PHPMailer` - This will create a new instance of PHPMailer.

3. `$mail->Host = 'smtp.zimbra.com'` - This will set the host of the Zimbra SMTP server.

4. `$mail->Port = 587` - This will set the port of the Zimbra SMTP server.

5. `$mail->SMTPAuth = true` - This will set the authentication type to use.

6. `$mail->Username = 'user@example.com'` - This will set the username to access the SMTP server.

7. `$mail->Password = 'password'` - This will set the password to access the SMTP server.

8. `$mail->Mailer = 'smtp'` - This will set the mailer type to use.

9. `$mail->send()` - This will send the mail.

**## Helpful links**

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [Zimbra SMTP Documentation](https://www.zimbra.com/docs/ne/latest/administration_guide/SMTP_Authentication.17.1.html)

onelinerhub: [How can I set up PHPMailer to use Zimbra SMTP?](https://onelinerhub.com/phpmailer/how-can-i-set-up-phpmailer-to-use-zimbra-smtp)