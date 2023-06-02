# How do I use the require_once function with PHPMailer?
// plain

The `require_once` function is used to include the PHPMailer library into a script. This allows the script to access the functions and classes contained in the library.

## Example code

```
<?php
require_once("PHPMailer/PHPMailerAutoload.php");

$mail = new PHPMailer;

$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'user@example.com';
$mail->Password = 'password';

$mail->From = 'from@example.com';
$mail->FromName = 'Sender Name';
$mail->addAddress('to@example.com', 'Receiver Name');

$mail->Subject = 'Test Email from PHPMailer';
$mail->Body    = 'This is a test email sent using PHPMailer.';

if(!$mail->send()) {
   echo 'Message could not be sent.';
   echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
   echo 'Message has been sent';
}
?>
```

## Output example

```
Message has been sent
```

## Code explanation

- `require_once("PHPMailer/PHPMailerAutoload.php");`: This line includes the PHPMailer library into the script.
- `$mail = new PHPMailer;`: This line creates a new PHPMailer object.
- `$mail->isSMTP();`: This line sets the mailer to use SMTP.
- `$mail->Host = 'smtp.example.com';`: This line sets the SMTP host.
- `$mail->SMTPAuth = true;`: This line enables SMTP authentication.
- `$mail->Username = 'user@example.com';`: This line sets the SMTP username.
- `$mail->Password = 'password';`: This line sets the SMTP password.
- `$mail->From = 'from@example.com';`: This line sets the From address.
- `$mail->FromName = 'Sender Name';`: This line sets the From name.
- `$mail->addAddress('to@example.com', 'Receiver Name');`: This line adds a recipient.
- `$mail->Subject = 'Test Email from PHPMailer';`: This line sets the email subject.
- `$mail->Body    = 'This is a test email sent using PHPMailer.';`: This line sets the email body.
- `if(!$mail->send()) { ... }`: This block sends the email and checks for errors.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)
- [require_once() Documentation](https://www.php.net/manual/en/function.require-once.php)

onelinerhub: [How do I use the require_once function with PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-use-the-require-once-function-with-phpmailer)