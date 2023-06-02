# How do I use PHPMailer with Google?
// plain

PHPMailer is a library for sending emails from PHP. It can be used with Google's SMTP server to send emails. Here is an example of how to use PHPMailer with Google:

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
    $mail->Host = 'smtp.gmail.com';                       // Specify main and backup SMTP servers
    $mail->SMTPAuth = true;                               // Enable SMTP authentication
    $mail->Username = 'user@gmail.com';                   // SMTP username
    $mail->Password = 'password';                         // SMTP password
    $mail->SMTPSecure = 'tls';                            // Enable TLS encryption, `ssl` also accepted
    $mail->Port = 587;                                    // TCP port to connect to

    //Recipients
    $mail->setFrom('from@example.com', 'Mailer');
    $mail->addAddress('joe@example.net', 'Joe User');     // Add a recipient
    $mail->addAddress('ellen@example.com');               // Name is optional
    $mail->addReplyTo('info@example.com', 'Information');
    $mail->addCC('cc@example.com');
    $mail->addBCC('bcc@example.com');

    //Content
    $mail->isHTML(true);                                  // Set email format to HTML
    $mail->Subject = 'Here is the subject';
    $mail->Body    = 'This is the HTML message body <b>in bold!</b>';
    $mail->AltBody = 'This is the body in plain text for non-HTML mail clients';

    $mail->send();
    echo 'Message has been sent';
} catch (Exception $e) {
    echo 'Message could not be sent. Mailer Error: ', $mail->ErrorInfo;
}
```

## Output example
 `Message has been sent`

## Code explanation

- `use PHPMailer\PHPMailer\PHPMailer;`: imports the PHPMailer class.
- `require 'vendor/autoload.php';`: loads Composer's autoloader.
- `$mail->SMTPDebug = 2;`: enables verbose debug output.
- `$mail->isSMTP();`: sets mailer to use SMTP.
- `$mail->Host = 'smtp.gmail.com';`: specifies main and backup SMTP servers.
- `$mail->SMTPAuth = true;`: enables SMTP authentication.
- `$mail->Username = 'user@gmail.com';`: sets SMTP username.
- `$mail->Password = 'password';`: sets SMTP password.
- `$mail->SMTPSecure = 'tls';`: enables TLS encryption.
- `$mail->Port = 587;`: sets TCP port to connect to.
- `$mail->setFrom('from@example.com', 'Mailer');`: sets the sender's address.
- `$mail->addAddress('joe@example.net', 'Joe User');`: adds a recipient's address.
- `$mail->addReplyTo('info@example.com', 'Information');`: sets the reply-to address.
- `$mail->addCC('cc@example.com');`: adds a carbon copy recipient.
- `$mail->addBCC('bcc@example.com');`: adds a blind carbon copy recipient.
- `$mail->isHTML(true);`: sets email format to HTML.
- `$mail->Subject = 'Here is the subject';`: sets the subject line.
- `$mail->Body    = 'This is the HTML message body <b>in bold!</b>';`: sets the HTML body of the message.
- `$mail->AltBody = 'This is the body in plain text for non-HTML mail clients';`: sets the plain text body of the message.
- `$mail->send();`: sends the message.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [Gmail SMTP Settings](https://support.google.com/a/answer/176600?hl=en)

onelinerhub: [How do I use PHPMailer with Google?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-with-google)