# How do I use PHPMailer to send emails?
// plain

PHPMailer is a library that can be used to send emails using PHP. It provides a simple and efficient way to send emails. The following example code will show how to use PHPMailer to send an email:

```
<?php
// Import PHPMailer classes into the global namespace
// These must be at the top of your script, not inside a function
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;
use PHPMailer\PHPMailer\Exception;

// Load Composer's autoloader
require 'vendor/autoload.php';

// Instantiation and passing `true` enables exceptions
$mail = new PHPMailer(true);

try {
    //Server settings
    $mail->SMTPDebug = SMTP::DEBUG_SERVER;                      // Enable verbose debug output
    $mail->isSMTP();                                            // Send using SMTP
    $mail->Host       = 'smtp1.example.com';                    // Set the SMTP server to send through
    $mail->SMTPAuth   = true;                                   // Enable SMTP authentication
    $mail->Username   = 'user@example.com';                     // SMTP username
    $mail->Password   = 'secret';                               // SMTP password
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;         // Enable TLS encryption; `PHPMailer::ENCRYPTION_SMTPS` encouraged
    $mail->Port       = 587;                                    // TCP port to connect to, use 465 for `PHPMailer::ENCRYPTION_SMTPS` above

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

This example code contains the following parts:

1. Importing the PHPMailer classes - This line of code imports the PHPMailer classes into the global namespace. This is necessary in order for the code to use the PHPMailer library.
2. Loading the autoloader - This line of code loads the autoloader, which is necessary in order for the code to use the PHPMailer library.
3. Instantiating the PHPMailer object - This line of code creates a new PHPMailer object, which is used to send emails.
4. Configuring the SMTP server - This section of code configures the SMTP server that will be used to send the email. It sets the host, authentication settings, encryption settings, and port.
5. Adding recipients - This section of code adds recipients to the email. It sets the from address, adds recipients, adds a reply-to address, and adds CC and BCC addresses.
6. Adding attachments - This section of code adds attachments to the email.
7. Adding content - This section of code adds the content of the email. It sets the format to HTML, adds a subject, adds a body, and adds an alternative body for non-HTML mail clients.
8. Sending the email - This line of code sends the email.

## Helpful links

- PHPMailer: https://github.com/PHPMailer/PHPMailer
- Composer: https://getcomposer.org/

onelinerhub: [How do I use PHPMailer to send emails?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-send-emails-1685707508)