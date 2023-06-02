# How can I use PHPMailer with XAMPP on Windows?
// plain

PHPMailer is an open-source library for sending emails through PHP code. It can be used with XAMPP on Windows to send emails from a local development environment. Here is an example of how to use PHPMailer with XAMPP on Windows:

```
// Require PHPMailer library
require_once('path/to/PHPMailer/PHPMailerAutoload.php');

// Create an instance of PHPMailer
$mail = new PHPMailer();

// Set SMTP configuration
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'example@example.com';
$mail->Password = 'password';
$mail->SMTPSecure = 'tls';
$mail->Port = 587;

// Set email content
$mail->setFrom('from@example.com', 'From Name');
$mail->addAddress('to@example.com', 'To Name');
$mail->Subject = 'PHPMailer on XAMPP';
$mail->Body = 'This is a test email sent using PHPMailer on XAMPP.';

// Send email
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

## Code explanation


1. Require PHPMailer library - includes the PHPMailer library from the specified path.
2. Create an instance of PHPMailer - creates a new instance of the PHPMailer class.
3. Set SMTP configuration - sets the SMTP configuration for the email.
4. Set email content - sets the from address, to address, subject and body of the email.
5. Send email - sends the email.

## Helpful links

- [PHPMailer Official Documentation](https://github.com/PHPMailer/PHPMailer/wiki)
- [XAMPP Official Documentation](https://www.apachefriends.org/faq_windows.html)

onelinerhub: [How can I use PHPMailer with XAMPP on Windows?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-with-xampp-on-windows)