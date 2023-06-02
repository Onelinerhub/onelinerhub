# How do I use PHPMailer to send a zip file?
// plain

Using PHPMailer to send a zip file is relatively easy. The following example code will send an email with a zip file attachment.

```
<?php

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'vendor/autoload.php';

$mail = new PHPMailer(true);

//Server settings
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'user@example.com';
$mail->Password = 'password';
$mail->SMTPSecure = 'tls';
$mail->Port = 587;

//Recipients
$mail->setFrom('from@example.com', 'Mailer');
$mail->addAddress('to@example.com', 'John Doe');

//Attachments
$mail->addAttachment('/path/to/zipfile.zip');

//Content
$mail->isHTML(true);
$mail->Subject = 'Here is the subject';
$mail->Body    = 'This is the HTML message body <b>in bold!</b>';
$mail->AltBody = 'This is the body in plain text for non-HTML mail clients';

$mail->send();

echo 'Message has been sent';
```

## Output example
 `Message has been sent`

The code consists of the following parts:

1. `use PHPMailer\PHPMailer\PHPMailer;` and `use PHPMailer\PHPMailer\Exception;` - imports the PHPMailer and Exception classes.
2. `require 'vendor/autoload.php';` - loads the autoloader which is used to load the classes.
3. `$mail = new PHPMailer(true);` - creates a new PHPMailer instance.
4. `$mail->isSMTP();` - sets the mailer to use SMTP.
5. `$mail->Host = 'smtp.example.com';` - sets the SMTP host.
6. `$mail->SMTPAuth = true;` - sets SMTP authentication.
7. `$mail->Username = 'user@example.com';` - sets SMTP username.
8. `$mail->Password = 'password';` - sets SMTP password.
9. `$mail->SMTPSecure = 'tls';` - sets security encryption.
10. `$mail->Port = 587;` - sets the SMTP port.
11. `$mail->setFrom('from@example.com', 'Mailer');` - sets the From address.
12. `$mail->addAddress('to@example.com', 'John Doe');` - sets the To address.
13. `$mail->addAttachment('/path/to/zipfile.zip');` - adds the zip file attachment.
14. `$mail->isHTML(true);` - sets the format of the email to HTML.
15. `$mail->Subject = 'Here is the subject';` - sets the subject of the email.
16. `$mail->Body    = 'This is the HTML message body <b>in bold!</b>';` - sets the body of the email.
17. `$mail->AltBody = 'This is the body in plain text for non-HTML mail clients';` - sets an alternate body for non-HTML email clients.
18. `$mail->send();` - sends the email.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)
- [PHPMailer Examples](https://github.com/PHPMailer/PHPMailer/tree/master/examples)

onelinerhub: [How do I use PHPMailer to send a zip file?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-send-a-zip-file)