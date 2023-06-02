# How do I use PHPMailer to send an email to multiple addresses?
// plain

Using PHPMailer to send an email to multiple addresses is quite simple. The following example code shows how to do it:

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
    //Recipients
    $mail->setFrom('from@example.com', 'Mailer');
    $mail->addAddress('recipient1@example.com', 'Recipient 1');
    $mail->addAddress('recipient2@example.com', 'Recipient 2');
    $mail->addAddress('recipient3@example.com', 'Recipient 3');
    $mail->addReplyTo('reply-to@example.com', 'Reply To');

    // Content
    $mail->isHTML(true);
    $mail->Subject = 'Here is the subject';
    $mail->Body    = 'This is the HTML message body <b>in bold!</b>';
    $mail->AltBody = 'This is the body in plain text for non-HTML mail clients';

    $mail->send();
    echo 'Message has been sent';
} catch (Exception $e) {
    echo "Message could not be sent. Mailer Error: {$mail->ErrorInfo}";
}
```

The output of this code will be `Message has been sent`.

The code consists of the following parts:
1. Importing the PHPMailer classes into the global namespace.
2. Loading Composer's autoloader.
3. Instantiating PHPMailer and passing `true` to enable exceptions.
4. Setting the sender of the email.
5. Adding recipients to the email.
6. Setting the content of the email.
7. Sending the email.
8. Outputting a message if the email was sent successfully.

## Helpful links
- [PHPMailer GitHub Repository](https://github.com/PHPMailer/PHPMailer)
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)

onelinerhub: [How do I use PHPMailer to send an email to multiple addresses?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-send-an-email-to-multiple-addresses)