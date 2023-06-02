# How can I use PHPMailer to send an HTML message?
// plain

Using PHPMailer to send an HTML message is a simple process. The following code example shows how to send an HTML message using PHPMailer:

```
<?php
  require 'PHPMailerAutoload.php';
  $mail = new PHPMailer;
  $mail->isSMTP();
  $mail->Host = 'smtp.example.com';
  $mail->SMTPAuth = true;
  $mail->Username = 'username';
  $mail->Password = 'password';
  $mail->SMTPSecure = 'tls';
  $mail->Port = 587;
  $mail->setFrom('from@example.com', 'Mailer');
  $mail->addAddress('to@example.com', 'Joe User');
  $mail->Subject = 'Here is the HTML message subject';
  $mail->msgHTML("<h1>Here is an HTML message</h1>");
  $mail->AltBody = 'This is the body in plain text for non-HTML mail clients';
  if (!$mail->send()) {
      echo "Message could not be sent.\n";
      echo "Mailer Error: " . $mail->ErrorInfo;
  } else {
      echo "Message has been sent";
  }
?>
```

## Output example
 `Message has been sent`

## Code explanation

- `require 'PHPMailerAutoload.php'` - This includes the PHPMailer library.
- `$mail = new PHPMailer;` - This creates a new PHPMailer instance.
- `$mail->isSMTP();` - This sets the mailer to use SMTP.
- `$mail->Host = 'smtp.example.com';` - This sets the SMTP host.
- `$mail->SMTPAuth = true;` - This enables SMTP authentication.
- `$mail->Username = 'username';` - This sets the SMTP username.
- `$mail->Password = 'password';` - This sets the SMTP password.
- `$mail->SMTPSecure = 'tls';` - This sets the SMTP security.
- `$mail->Port = 587;` - This sets the SMTP port.
- `$mail->setFrom('from@example.com', 'Mailer');` - This sets the From address.
- `$mail->addAddress('to@example.com', 'Joe User');` - This sets the To address.
- `$mail->Subject = 'Here is the HTML message subject';` - This sets the subject.
- `$mail->msgHTML("<h1>Here is an HTML message</h1>");` - This sets the HTML message body.
- `$mail->AltBody = 'This is the body in plain text for non-HTML mail clients';` - This sets the plain text message body.
- `if (!$mail->send()) { ... } else { ... }` - This sends the message and checks for errors.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/blob/master/docs/README.md)
- [PHPMailer Quick Start Guide](https://github.com/PHPMailer/PHPMailer/blob/master/docs/quickstart.md)

onelinerhub: [How can I use PHPMailer to send an HTML message?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-to-send-an-html-message)