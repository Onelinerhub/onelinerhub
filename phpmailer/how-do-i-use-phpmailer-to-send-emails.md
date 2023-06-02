# How do I use PHPMailer to send emails?
// plain

PHPMailer is a popular library for sending emails with PHP. To use it, you need to include the library in your code and configure your email settings. Here is an example code block to send a simple email using PHPMailer:

```
<?php
  // Include PHPMailer library
  require_once 'PHPMailer/PHPMailerAutoload.php';

  // Create a new PHPMailer instance
  $mail = new PHPMailer;

  // Configure SMTP settings
  $mail->isSMTP();
  $mail->Host = 'smtp.example.com';
  $mail->SMTPAuth = true;
  $mail->Username = 'username@example.com';
  $mail->Password = 'password';

  // Set sender and recipient
  $mail->setFrom('sender@example.com', 'Sender Name');
  $mail->addAddress('recipient@example.com', 'Recipient Name');

  // Set mail subject and body
  $mail->Subject = 'Test email';
  $mail->Body = 'This is a test email sent using PHPMailer.';

  // Send email
  if(!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
  } else {
    echo 'Message has been sent';
  }
?>
```

## Output example
 `Message has been sent`

## Code explanation

- `require_once 'PHPMailer/PHPMailerAutoload.php';`: Include the PHPMailer library.
- `$mail = new PHPMailer;`: Create a new PHPMailer instance.
- `$mail->isSMTP();`: Configure the mailer to use SMTP.
- `$mail->Host = 'smtp.example.com';`: Set the SMTP server.
- `$mail->SMTPAuth = true;`: Enable SMTP authentication.
- `$mail->Username = 'username@example.com';`: Set SMTP username.
- `$mail->Password = 'password';`: Set SMTP password.
- `$mail->setFrom('sender@example.com', 'Sender Name');`: Set the sender.
- `$mail->addAddress('recipient@example.com', 'Recipient Name');`: Set the recipient.
- `$mail->Subject = 'Test email';`: Set the subject.
- `$mail->Body = 'This is a test email sent using PHPMailer.';`: Set the body.
- `if(!$mail->send()) {`: Send the email.

## Helpful links
- [PHPMailer GitHub page](https://github.com/PHPMailer/PHPMailer)
- [PHPMailer official website](https://phpmailer.github.io/)

onelinerhub: [How do I use PHPMailer to send emails?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-send-emails)