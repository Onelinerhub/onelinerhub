# How can I use PHPMailer with XAMPP on a localhost?
// plain

PHPMailer is a library used to send emails using PHP. It can be used with XAMPP on a localhost by following these steps:

1. Download and install XAMPP.
2. Download and install PHPMailer from [Github](https://github.com/PHPMailer/PHPMailer).
3. Create a new file, for example `mailer.php`, and include the PHPMailer library:
```
<?php
    require 'path/to/PHPMailer/src/PHPMailer.php';
    require 'path/to/PHPMailer/src/SMTP.php';
?>
```
4. Create a new instance of the PHPMailer class and set the necessary parameters:
```
<?php
    //Create a new PHPMailer instance
    $mail = new PHPMailer;
    //Set who the message is to be sent from
    $mail->setFrom('from@example.com', 'First Last');
    //Set an alternative reply-to address
    $mail->addReplyTo('replyto@example.com', 'First Last');
    //Set who the message is to be sent to
    $mail->addAddress('whoto@example.com', 'John Doe');
    //Set the subject line
    $mail->Subject = 'PHPMailer XAMPP test';
    //Read an HTML message body from an external file, convert referenced images to embedded,
    //convert HTML into a basic plain-text alternative body
    $mail->msgHTML(file_get_contents('contents.html'), __DIR__);
    //Replace the plain text body with one created manually
    $mail->AltBody = 'This is a plain-text message body';
?>
```
5. Finally, send the mail:
```
<?php
    //send the message, check for errors
    if (!$mail->send()) {
        echo "Mailer Error: " . $mail->ErrorInfo;
    } else {
        echo "Message sent!";
    }
?>
```
6. Start the XAMPP server and open the `mailer.php` file in a browser to send the email.
7. Check the inbox of the recipient to see if the mail has been sent successfully.

## Helpful links
- [Official PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)
- [XAMPP Official Website](https://www.apachefriends.org/index.html)

onelinerhub: [How can I use PHPMailer with XAMPP on a localhost?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-with-xampp-on-a-localhost)