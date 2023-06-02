# How can I use PHPMailer with Drupal?
// plain

Using PHPMailer with Drupal is a quick and easy way to send emails from your Drupal site. The following example code shows how to use PHPMailer in your Drupal site:

```
<?php
// Include PHPMailer library
require 'PHPMailer/PHPMailerAutoload.php';

// Create new PHPMailer instance
$mail = new PHPMailer;

// Set mailer to use SMTP
$mail->isSMTP();

// Specify main and backup SMTP servers
$mail->Host = 'smtp1.example.com;smtp2.example.com';

// Enable SMTP authentication
$mail->SMTPAuth = true;

// SMTP username
$mail->Username = 'user@example.com';

// SMTP password
$mail->Password = 'secret';

// Set from address
$mail->setFrom('from@example.com', 'Mailer');

// Set to address
$mail->addAddress('recipient@example.com', 'John Doe');

// Set subject
$mail->Subject = 'Here is the subject';

// Set body
$mail->Body = 'This is the HTML message body <b>in bold!</b>';

// Send email
if (!$mail->send()) {
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

The code above will send an email from `from@example.com` to `recipient@example.com` using SMTP authentication and the specified SMTP servers. The email will have the subject `Here is the subject` and the body `This is the HTML message body <b>in bold!</b>`.

## Code explanation


- `require 'PHPMailer/PHPMailerAutoload.php';`: This line includes the PHPMailer library.
- `$mail = new PHPMailer;`: This line creates a new PHPMailer instance.
- `$mail->isSMTP();`: This line sets the mailer to use SMTP.
- `$mail->Host = 'smtp1.example.com;smtp2.example.com';`: This line specifies the main and backup SMTP servers.
- `$mail->SMTPAuth = true;`: This line enables SMTP authentication.
- `$mail->Username = 'user@example.com';`: This line sets the SMTP username.
- `$mail->Password = 'secret';`: This line sets the SMTP password.
- `$mail->setFrom('from@example.com', 'Mailer');`: This line sets the from address.
- `$mail->addAddress('recipient@example.com', 'John Doe');`: This line sets the to address.
- `$mail->Subject = 'Here is the subject';`: This line sets the subject.
- `$mail->Body = 'This is the HTML message body <b>in bold!</b>';`: This line sets the body.
- `if (!$mail->send()) {`: This line checks if the email was sent successfully.
- `echo 'Message could not be sent.';`: This line prints an error message if the email was not sent successfully.
- `echo 'Message has been sent';`: This line prints a success message if the email was sent successfully.

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/blob/master/docs/README.md)
- [Drupal Documentation](https://www.drupal.org/docs/7)

onelinerhub: [How can I use PHPMailer with Drupal?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-with-drupal)