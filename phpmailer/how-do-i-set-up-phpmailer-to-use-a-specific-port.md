# How do I set up PHPMailer to use a specific port?
// plain

To set up PHPMailer to use a specific port, the following steps should be taken:

1. Include the PHPMailer library in your project.

```
require 'PHPMailer/PHPMailerAutoload.php';
```

2. Create a new instance of the PHPMailer class.

```
$mail = new PHPMailer;
```

3. Set the port that you wish to use.

```
$mail->Port = 465;
```

4. Set the encryption type to use for the port.

```
$mail->SMTPSecure = 'ssl';
```

5. Connect to the SMTP server using the provided port and encryption type.

```
$mail->Host = 'smtp.example.com';
$mail->Port = 465;
$mail->SMTPSecure = 'ssl';
$mail->SMTPAuth = true;
```

6. Send the mail using the `send()` method.

```
$mail->send();
```

7. Check for errors.

```
if (!$mail->send()) {
    echo 'Mailer Error: ' . $mail->ErrorInfo;
}
```

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [SMTP Port Numbers](https://www.arclab.com/en/kb/email/list-of-smtp-and-pop3-servers-mailserver-list.html)

onelinerhub: [How do I set up PHPMailer to use a specific port?](https://onelinerhub.com/phpmailer/how-do-i-set-up-phpmailer-to-use-a-specific-port)