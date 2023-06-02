# How can I use PHPMailer to send emails from a localhost server?
// plain

PHPMailer is a library for sending emails from a localhost server using PHP. It can be used to send emails from a web server or from a command line script. Here is an example of how to use PHPMailer to send an email from a localhost server:

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
    $mail->SMTPDebug = 0;                                       // Enable verbose debug output
    $mail->isSMTP();                                            // Set mailer to use SMTP
    $mail->Host       = 'localhost';                            // Specify main and backup SMTP servers
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

## Output example
 `Message has been sent`

The code above consists of the following parts:

1. Importing PHPMailer classes into the global namespace: This allows the code to access the PHPMailer classes.
2. Loading Composer's autoloader: This loads the necessary files for PHPMailer.
3. Instantiating the PHPMailer object: This creates a new PHPMailer object that will be used to send the email.
4. Setting the server settings: This sets the SMTP server, username, password, encryption, and port for the SMTP server.
5. Adding the recipients: This adds the recipients of the email.
6. Adding attachments: This adds any attachments that need to be included with the email.
7. Setting the content: This sets the subject, body, and other content for the email.
8. Sending the email: This sends the email.

For more information about PHPMailer and how to use it, see the [official documentation](https://github.com/PHPMailer/PHPMailer/wiki).

onelinerhub: [How can I use PHPMailer to send emails from a localhost server?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-to-send-emails-from-a-localhost-server)