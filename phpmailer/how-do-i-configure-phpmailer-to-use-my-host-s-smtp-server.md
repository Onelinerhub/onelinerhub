# How do I configure PHPMailer to use my host's SMTP server?
// plain

PHPMailer is a library for sending emails from PHP code. It can be configured to use a host's SMTP server to send emails. Here is an example of how to configure PHPMailer to use an SMTP server:

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
    $mail->SMTPSecure = PHPMailer::ENCRYPTION_STARTTLS;         // Enable TLS encryption; `PHPMailer::ENCRYPTION_SMTPS` also accepted
    $mail->Port       = 587;                                    // TCP port to connect to

    //Recipients
    $mail->setFrom('from@example.com', 'Mailer');
    $mail->addAddress('joe@example.net', 'Joe User');     // Add a recipient

    // Content
    $mail->isHTML(true);                                  // Set email format to HTML
    $mail->Subject = 'Here is the subject';
    $mail->Body    = 'This is the HTML message body <b>in bold!</b>';

    $mail->send();
    echo 'Message has been sent';
} catch (Exception $e) {
    echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo}";
}
```

This example code will configure PHPMailer to use the SMTP server at `smtp.example.com`, with authentication enabled using the username `user@example.com` and password `secret`. The connection will be secured using TLS encryption on port 587.

The code sets the sender address to `from@example.com` and adds a recipient address `joe@example.net`. It then sets the email content to an HTML message with the subject line `Here is the subject` and body `This is the HTML message body <b>in bold!</b>`.

If the code runs successfully, it will output `Message has been sent`.

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [SMTP Configuration](https://github.com/PHPMailer/PHPMailer/wiki/SMTP-Configuration)

onelinerhub: [How do I configure PHPMailer to use my host's SMTP server?](https://onelinerhub.com/phpmailer/how-do-i-configure-phpmailer-to-use-my-host-s-smtp-server)