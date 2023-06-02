# How do I test PHPMailer?
// plain

Testing PHPMailer involves verifying that the script is correctly configured and that emails are being sent correctly.

To test PHPMailer, you can use the following example code:

```
<?php
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
    $mail->Host       = 'smtp1.example.com';  // Specify main and backup SMTP servers
    $mail->SMTPAuth   = true;                                   // Enable SMTP authentication
    $mail->Username   = 'user@example.com';                     // SMTP username
    $mail->Password   = 'secret';                               // SMTP password
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

The output of the example code should be `Message has been sent`.

The code consists of the following parts:

1. Importing PHPMailer classes: `use PHPMailer\PHPMailer\PHPMailer;` and `use PHPMailer\PHPMailer\Exception;`
2. Loading Composer's autoloader: `require 'vendor/autoload.php';`
3. Instantiating the PHPMailer class: `$mail = new PHPMailer(true);`
4. Configuring the SMTP server: `$mail->SMTPDebug = 2;`, `$mail->isSMTP();`, `$mail->Host = 'smtp1.example.com';`, `$mail->SMTPAuth = true;`, `$mail->Username = 'user@example.com';`, `$mail->Password = 'secret';`, `$mail->SMTPSecure = 'tls';`, `$mail->Port = 587;`
5. Adding recipients: `$mail->setFrom('from@example.com', 'Mailer');`, `$mail->addAddress('joe@example.net', 'Joe User');`, `$mail->addAddress('ellen@example.com');`, `$mail->addReplyTo('info@example.com', 'Information');`, `$mail->addCC('cc@example.com');`, `$mail->addBCC('bcc@example.com');`
6. Adding attachments: `$mail->addAttachment('/var/tmp/file.tar.gz');`, `$mail->addAttachment('/tmp/image.jpg', 'new.jpg');`
7. Setting content: `$mail->isHTML(true);`, `$mail->Subject = 'Here is the subject';`, `$mail->Body = 'This is the HTML message body <b>in bold!</b>';`, `$mail->AltBody = 'This is the body in plain text for non-HTML mail clients';`
8. Sending the email: `$mail->send();`

## Helpful links

* [PHPMailer GitHub page](https://github.com/PHPMailer/PHPMailer)
* [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)
* [PHPMailer Examples](https://github.com/PHPMailer/PHPMailer/tree/master/examples)

onelinerhub: [How do I test PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-test-phpmailer)