# How can I use PHPMailer to send emails with a Yahoo account?
// plain

To use PHPMailer to send emails with a Yahoo account, you will need to set the SMTP host, port, and authentication settings. Here is an example code block to do so:

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
    $mail->Host       = 'smtp.mail.yahoo.com';                  // Specify Yahoo SMTP server
    $mail->SMTPAuth   = true;                                   // Enable SMTP authentication
    $mail->Username   = 'YOUR_YAHOO_EMAIL_ADDRESS';             // SMTP username
    $mail->Password   = 'YOUR_YAHOO_EMAIL_PASSWORD';             // SMTP password
    $mail->SMTPSecure = 'tls';                                  // Enable TLS encryption, `ssl` also accepted
    $mail->Port       = 587;                                    // TCP port to connect to

    //Recipients
    $mail->setFrom('YOUR_YAHOO_EMAIL_ADDRESS', 'Your Name');
    $mail->addAddress('RECIPIENT_EMAIL_ADDRESS', 'Recipient Name');     // Add a recipient

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

This example code block will set the SMTP host to `smtp.mail.yahoo.com`, enable SMTP authentication, set the username and password to your Yahoo email address and password, set the encryption to TLS, and set the port to 587. The code will also set the sender and recipient email addresses, set the subject and body of the email, and send the email. If the email is successfully sent, the output will be `Message has been sent`.

## Code explanation


1. `use PHPMailer\PHPMailer\PHPMailer;` and `use PHPMailer\PHPMailer\Exception;`: These two lines import the PHPMailer classes into the global namespace.
2. `require 'vendor/autoload.php';`: This line loads the Composer autoloader.
3. `$mail->SMTPDebug = 2;`: This line enables verbose debug output.
4. `$mail->isSMTP();`: This line sets the mailer to use SMTP.
5. `$mail->Host = 'smtp.mail.yahoo.com';`: This line sets the SMTP host to `smtp.mail.yahoo.com`.
6. `$mail->SMTPAuth = true;`: This line enables SMTP authentication.
7. `$mail->Username = 'YOUR_YAHOO_EMAIL_ADDRESS';` and `$mail->Password = 'YOUR_YAHOO_EMAIL_PASSWORD';`: These two lines set the username and password to your Yahoo email address and password.
8. `$mail->SMTPSecure = 'tls';`: This line sets the encryption to TLS.
9. `$mail->Port = 587;`: This line sets the port to 587.
10. `$mail->setFrom('YOUR_YAHOO_EMAIL_ADDRESS', 'Your Name');` and `$mail->addAddress('RECIPIENT_EMAIL_ADDRESS', 'Recipient Name');`: These two lines set the sender and recipient email addresses.
11. `$mail->isHTML(true);`: This line sets the email format to HTML.
12. `$mail->Subject = 'Here is the subject';` and `$mail->Body = 'This is the HTML message body <b>in bold!</b>';`: These two lines set the subject and body of the email.
13. `$mail->send();`: This line sends the email.
14. `echo 'Message has been sent';`: This line prints the output `Message has been sent` if the email is successfully sent.

## Helpful links

- [PHPMailer official documentation](https://github.com/PHPMailer/PHPMailer)
- [Yahoo SMTP server settings](https://help.yahoo.com/kb/SLN7253.html)

onelinerhub: [How can I use PHPMailer to send emails with a Yahoo account?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-to-send-emails-with-a-yahoo-account)