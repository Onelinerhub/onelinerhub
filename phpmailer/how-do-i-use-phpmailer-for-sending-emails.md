# How do I use PHPMailer for sending emails?
// plain

PHPMailer is a popular open source library for sending emails with PHP. To use it, you will need to install it using Composer:

```
composer require phpmailer/phpmailer
```

Once installed, you can use the following code to send an email:

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
    $mail->Host = 'smtp1.example.com';  // Specify main and backup SMTP servers
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

The code above does the following:

1. Imports the PHPMailer classes into the global namespace.
2. Loads the Composer autoloader.
3. Sets the SMTP server settings.
4. Sets the recipient information.
5. Attaches any files.
6. Sets the email format to HTML.
7. Sets the subject and body of the email.
8. Sends the email.

If successful, it will output `Message has been sent`.

For more information, see the PHPMailer [documentation](https://github.com/PHPMailer/PHPMailer/tree/master/docs).

onelinerhub: [How do I use PHPMailer for sending emails?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-for-sending-emails)