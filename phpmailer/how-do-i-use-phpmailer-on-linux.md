# How do I use PHPMailer on Linux?
// plain

PHPMailer is a library for sending emails from PHP code. It can be used on Linux systems to send emails through an SMTP server.

The following example shows how to use PHPMailer to send an email from a Linux system:

```php
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

    //Attachments
    $mail->addAttachment('/var/tmp/file.tar.gz');         // Add attachments
    $mail->addAttachment('/tmp/image.jpg', 'new.jpg');    // Optional name

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

```
Message has been sent
```

The code above can be broken down into the following parts:

1. Import PHPMailer classes into the global namespace: This imports the necessary classes from the PHPMailer library.
2. Load Composer's autoloader: This loads the autoloader from the Composer dependency manager.
3. Create a PHPMailer instance: This creates an instance of the PHPMailer class.
4. Configure the SMTP server: This configures the SMTP server settings, such as host, authentication, and port.
5. Add recipients: This adds the recipients of the email, such as the from address, to address, cc, and bcc.
6. Add attachments: This adds attachments to the email, if necessary.
7. Set content: This sets the content of the email, such as the subject, body, and alt body.
8. Send the email: This sends the email.

For more information, please see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki) and [Composer documentation](https://getcomposer.org/doc/).

onelinerhub: [How do I use PHPMailer on Linux?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-on-linux)