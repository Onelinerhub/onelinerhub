# How can I use PHPMailer to send emails from my localhost?
// plain

PHPMailer is a popular open source library used for sending emails from PHP scripts. It can be used to send emails from localhost using SMTP.

## Example code

```
<?php
// Import PHPMailer classes into the global namespace
// These must be at the top of your script, not inside a function
use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\SMTP;

// Load Composer's autoloader
require 'vendor/autoload.php';

// Instantiation and passing `true` enables exceptions
$mail = new PHPMailer(true);

try {
    //Server settings
    $mail->SMTPDebug = SMTP::DEBUG_SERVER;                      // Enable verbose debug output
    $mail->isSMTP();                                            // Send using SMTP
    $mail->Host       = 'smtp.example.com';                    // Set the SMTP server to send through
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

## Code explanation

1. Import PHPMailer classes into the global namespace - This imports the PHPMailer classes into the global namespace, making them available for use in the script.
2. Load Composer's autoloader - This loads the Composer autoloader, which is used to load the PHPMailer classes.
3. Instantiation and passing `true` enables exceptions - This instantiates the PHPMailer class and enables exceptions, which can be used to catch errors.
4. Server settings - This sets the SMTP server to send through, enables SMTP authentication, sets the SMTP username and password, enables encryption, and sets the port to connect to.
5. Recipients - This sets the from address, adds recipients, adds a reply-to address, adds CC and BCC recipients, and sets the recipient's name (optional).
6. Attachments - This adds attachments to the email.
7. Content - This sets the email format to HTML, sets the subject, sets the body, and sets the alt body.

## Helpful links

- [PHPMailer GitHub page](https://github.com/PHPMailer/PHPMailer)
- [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial)

onelinerhub: [How can I use PHPMailer to send emails from my localhost?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-to-send-emails-from-my-localhost)