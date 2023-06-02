# How can I send emails using PHPMailer without a password?
// plain

You can send emails using PHPMailer without a password by using a third-party email service such as SendGrid. This is done by configuring PHPMailer to use SMTP authentication with the third-party service.

## Example code

```
<?php
// Import PHPMailer classes into the global namespace
// These must be at the top of your script, not inside a function
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

//Load Composer's autoloader
require 'vendor/autoload.php';

$mail = new PHPMailer(true);                              // Passing `true` enables exceptions
try {
    //Server settings
    $mail->SMTPDebug = 2;                                 // Enable verbose debug output
    $mail->isSMTP();                                      // Set mailer to use SMTP
    $mail->Host = 'smtp.sendgrid.net';                    // Specify main and backup SMTP servers
    $mail->SMTPAuth = true;                               // Enable SMTP authentication
    $mail->Username = 'apikey';                           // SMTP username
    $mail->Password = 'SG.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'; // SMTP password
    $mail->SMTPSecure = 'tls';                            // Enable TLS encryption, `ssl` also accepted
    $mail->Port = 587;                                    // TCP port to connect to

    //Recipients
    $mail->setFrom('from@example.com', 'Mailer');
    $mail->addAddress('joe@example.net', 'Joe User');     // Add a recipient

    //Content
    $mail->isHTML(true);                                  // Set email format to HTML
    $mail->Subject = 'Here is the subject';
    $mail->Body    = 'This is the HTML message body <b>in bold!</b>';

    $mail->send();
    echo 'Message has been sent';
} catch (Exception $e) {
    echo 'Message could not be sent. Mailer Error: ', $mail->ErrorInfo;
}
```

## Output example

```
Message has been sent
```

## Code explanation


- `use PHPMailer\PHPMailer\PHPMailer;`: This is used to import the PHPMailer classes into the global namespace.
- `require 'vendor/autoload.php';`: This is used to load Composer's autoloader.
- `$mail->SMTPDebug = 2;`: This is used to enable verbose debug output.
- `$mail->isSMTP();`: This is used to set the mailer to use SMTP.
- `$mail->Host = 'smtp.sendgrid.net';`: This is used to specify the main and backup SMTP servers.
- `$mail->SMTPAuth = true;`: This is used to enable SMTP authentication.
- `$mail->Username = 'apikey';`: This is used to set the SMTP username.
- `$mail->Password = 'SG.xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx';`: This is used to set the SMTP password.
- `$mail->SMTPSecure = 'tls';`: This is used to enable TLS encryption.
- `$mail->Port = 587;`: This is used to set the TCP port to connect to.
- `$mail->setFrom('from@example.com', 'Mailer');`: This is used to set the sender of the email.
- `$mail->addAddress('joe@example.net', 'Joe User');`: This is used to add a recipient to the email.
- `$mail->isHTML(true);`: This is used to set the email format to HTML.
- `$mail->Subject = 'Here is the subject';`: This is used to set the subject of the email.
- `$mail->Body    = 'This is the HTML message body <b>in bold!</b>';`: This is used to set the body of the email.
- `$mail->send();`: This is used to send the email.

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)
- [SendGrid Documentation](https://sendgrid.com/docs/)

onelinerhub: [How can I send emails using PHPMailer without a password?](https://onelinerhub.com/phpmailer/how-can-i-send-emails-using-phpmailer-without-a-password)