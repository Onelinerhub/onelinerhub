# How can I use PHPMailer to send emails through Outlook?
// plain

PHPMailer is a library that allows you to send emails via SMTP, POP3, or IMAP. You can use it to send emails through Outlook by configuring it to use Outlook's SMTP server.

The following example code shows how to send an email using PHPMailer and Outlook's SMTP server:

```php
// Import PHPMailer classes into the global namespace
// These must be at the top of your script, not inside a function
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Load Composer's autoloader
require 'vendor/autoload.php';

// Instantiation and passing `true` enables exceptions
$mail = new PHPMailer(true);

try {
    //Server settings
    $mail->SMTPDebug = 2;                                       // Enable verbose debug output
    $mail->isSMTP();                                            // Set mailer to use SMTP
    $mail->Host       = 'smtp-mail.outlook.com';                // Specify Outlook's SMTP server
    $mail->SMTPAuth   = true;                                   // Enable SMTP authentication
    $mail->Username   = 'user@example.com';                     // Outlook username
    $mail->Password   = 'secret';                               // Outlook password
    $mail->SMTPSecure = 'tls';                                  // Enable TLS encryption, `ssl` also accepted
    $mail->Port       = 587;                                    // TCP port to connect to

    //Recipients
    $mail->setFrom('from@example.com', 'Mailer');
    $mail->addAddress('joe@example.net', 'Joe User');     // Add a recipient
    $mail->addAddress('ellen@example.com');               // Name is optional
    $mail->addReplyTo('info@example.com', 'Information');
    $mail->addCC('cc@example.com');
    $mail->addBCC('bcc@example.com');

    // Attachments
    $mail->addAttachment('/var/tmp/file.tar.gz');         // Add attachments
    $mail->addAttachment('/tmp/image.jpg', 'new.jpg');    // Optional name

    // Content
    $mail->isHTML(true);                                  // Set email format to HTML
    $mail->Subject = 'Here is the subject';
    $mail->Body    = 'This is the HTML message body <b>in bold!</b>';
    $mail->AltBody = 'This is the body in plain text for non-HTML mail clients';

    $mail->send();
    echo 'Message has been sent';
} catch (Exception $e) {
    echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo}";
}
```

The code above will output `Message has been sent` if the email is sent successfully.

The code consists of the following parts:

1. `use PHPMailer\PHPMailer\PHPMailer;` and `use PHPMailer\PHPMailer\Exception;`: These lines import the PHPMailer classes into the global namespace.
2. `require 'vendor/autoload.php';`: This line loads the Composer autoloader.
3. `$mail = new PHPMailer(true);`: This line instantiates the PHPMailer object, and passing `true` enables exceptions.
4. `$mail->SMTPDebug = 2;`: This line sets the SMTP debug level to 2, which will output verbose debug output.
5. `$mail->isSMTP();`: This line sets the mailer to use SMTP.
6. `$mail->Host = 'smtp-mail.outlook.com';`: This line sets Outlook's SMTP server.
7. `$mail->SMTPAuth = true;`: This line enables SMTP authentication.
8. `$mail->Username = 'user@example.com';` and `$mail->Password = 'secret';`: These lines set the Outlook username and password.
9. `$mail->SMTPSecure = 'tls';`: This line enables TLS encryption.
10. `$mail->Port = 587;`: This line sets the TCP port to connect to.
11. `$mail->setFrom('from@example.com', 'Mailer');`: This line sets the sender of the email.
12. `$mail->addAddress('joe@example.net', 'Joe User');`: This line adds a recipient to the email.
13. `$mail->addReplyTo('info@example.com', 'Information');`: This line sets the reply-to address.
14. `$mail->addCC('cc@example.com');` and `$mail->addBCC('bcc@example.com');`: These lines add CC and BCC recipients to the email.
15. `$mail->addAttachment('/var/tmp/file.tar.gz');` and `$mail->addAttachment('/tmp/image.jpg', 'new.jpg');`: These lines add attachments to the email.
16. `$mail->isHTML(true);`: This line sets the email format to HTML.
17. `$mail->Subject = 'Here is the subject';`: This line sets the subject of the email.
18. `$mail->Body = 'This is the HTML message body <b>in bold!</b>';` and `$mail->AltBody = 'This is the body in plain text for non-HTML mail clients';`: These lines set the body of the email.
19. `$mail->send();`: This line sends the email.

For more information about PHPMailer, see the [official documentation](https://github.com/PHPMailer/PHPMailer/).

onelinerhub: [How can I use PHPMailer to send emails through Outlook?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-to-send-emails-through-outlook)