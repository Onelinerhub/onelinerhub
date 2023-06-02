# How do I send emails using PHPMailer and Mailjet?
// plain

Using PHPMailer and Mailjet, you can send emails programmatically. Here is an example code snippet to get you started:

```
<?php
require 'PHPMailer/PHPMailerAutoload.php';

$mail = new PHPMailer;

//Server settings
$mail->SMTPDebug = 0;                      // Enable verbose debug output
$mail->isSMTP();                                            // Set mailer to use SMTP
$mail->Host = 'in.mailjet.com';  // Specify main and backup SMTP servers
$mail->SMTPAuth = true;                                   // Enable SMTP authentication
$mail->Username = 'your_mailjet_username';                 // SMTP username
$mail->Password = 'your_mailjet_password';                           // SMTP password
$mail->SMTPSecure = 'tls';                            // Enable TLS encryption, `ssl` also accepted
$mail->Port = 587;                                    // TCP port to connect to

//Recipients
$mail->setFrom('from@example.com', 'Mailer');
$mail->addAddress('recipient@example.com', 'John Doe');     // Add a recipient

//Content
$mail->isHTML(true);                                  // Set email format to HTML
$mail->Subject = 'Here is the subject';
$mail->Body    = 'This is the HTML message body <b>in bold!</b>';
$mail->AltBody = 'This is the body in plain text for non-HTML mail clients';

if(!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
?>
```

This code will send an email with HTML body and plain text body. It will also output a message if the email was sent successfully or if there was an error.

The code consists of the following parts:

1. Requiring the PHPMailer library
2. Setting up the SMTP server details
3. Setting up the sender and recipient
4. Setting up the email content (subject, HTML body, plain text body)
5. Sending the email and checking the result

You can find more information about using PHPMailer and Mailjet [here](https://github.com/PHPMailer/PHPMailer/blob/master/docs/examples/mailjet.phps).

onelinerhub: [How do I send emails using PHPMailer and Mailjet?](https://onelinerhub.com/phpmailer/how-do-i-send-emails-using-phpmailer-and-mailjet)