# email

How do I use PHPMailer to send an HTML email?
// plain

PHPMailer is a library for sending emails from PHP. It can be used to send HTML emails by setting the `IsHTML` property to `true` and using the `MsgHTML` property to set the HTML content of the email.

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
    $mail->Host = 'smtp1.example.com;smtp2.example.com';  // Specify main and backup SMTP servers
    $mail->SMTPAuth = true;                               // Enable SMTP authentication
    $mail->Username = 'user@example.com';                 // SMTP username
    $mail->Password = 'secret';                           // SMTP password
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
    $mail->IsHTML(true);                                  // Set email format to HTML
    $mail->Subject = 'Here is the subject';
    $mail->Body    = 'This is the HTML message body <b>in bold!</b>';
    $mail->AltBody = 'This is the body in plain text for non-HTML mail clients';

    $mail->send();
    echo 'Message has been sent';
} catch (Exception $e) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
}
```

Output (if any): `Message has been sent`

## Code explanation

1. `use PHPMailer\PHPMailer\PHPMailer;` - This imports the PHPMailer classes into the global namespace.
2. `require 'vendor/autoload.php';` - This loads the Composer autoloader.
3. `$mail = new PHPMailer(true);` - This creates a new instance of the PHPMailer class.
4. `$mail->SMTPDebug = 2;` - This enables verbose debugging output.
5. `$mail->isSMTP();` - This sets the mailer to use SMTP.
6. `$mail->Host = 'smtp1.example.com;smtp2.example.com';` - This specifies the main and backup SMTP servers.
7. `$mail->SMTPAuth = true;` - This enables SMTP authentication.
8. `$mail->Username = 'user@example.com';` - This sets the SMTP username.
9. `$mail->Password = 'secret';` - This sets the SMTP password.
10. `$mail->SMTPSecure = 'tls';` - This enables TLS encryption.
11. `$mail->Port = 587;` - This sets the TCP port to connect to.
12. `$mail->setFrom('from@example.com', 'Mailer');` - This sets the sender of the email.
13. `$mail->addAddress('joe@example.net', 'Joe User');` - This adds a recipient to the email.
14. `$mail->addReplyTo('info@example.com', 'Information');` - This sets the reply-to address of the email.
15. `$mail->addCC('cc@example.com');` - This adds a carbon copy recipient to the email.
16. `$mail->addBCC('bcc@example.com');` - This adds a blind carbon copy recipient to the email.
17. `$mail->IsHTML(true);` - This sets the email format to HTML.
18. `$mail->Subject = 'Here is the subject';` - This sets the subject of the email.
19. `$mail->Body    = 'This is the HTML message body <b>in bold!</b>';` - This sets the HTML content of the email.
20. `$mail->AltBody = 'This is the body in plain text for non-HTML mail clients';` - This sets the plain text content of the email.
21. `$mail->send();` - This sends the email.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)

onelinerhub: [email

How do I use PHPMailer to send an HTML email?](https://onelinerhub.com/phpmailer/email--how-do-i-use-phpmailer-to-send-an-html-email)