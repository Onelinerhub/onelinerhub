# How do I decide between using PHPMailer and Symfony Mailer for sending emails?
// plain

When deciding between PHPMailer and Symfony Mailer for sending emails, it is important to consider your specific project requirements.

For example, PHPMailer is a standalone library, while Symfony Mailer is a component of the Symfony framework. If you are already using Symfony, then Symfony Mailer may be the more logical choice.

PHPMailer is also better suited for sending plain text emails, while Symfony Mailer is better for sending HTML emails.

Below is an example of using PHPMailer to send an email:

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
    $mail->Host = 'smtp1.example.com;smtp2.example.com';  // Specify main and backup SMTP servers
    $mail->SMTPAuth = true;                               // Enable SMTP authentication
    $mail->Username = 'user@example.com';                 // SMTP username
    $mail->Password = 'secret';                           // SMTP password
    $mail->SMTPSecure = 'tls';                            // Enable TLS encryption, `ssl` also accepted
    $mail->Port = 587;                                    // TCP port to connect to

    //Recipients
    $mail->setFrom('from@example.com', 'Mailer');
    $mail->addAddress('joe@example.net', 'Joe User');     // Add a recipient

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

In conclusion, the choice between PHPMailer and Symfony Mailer will depend on the specific requirements of your project.

## Helpful links

- [PHPMailer](https://github.com/PHPMailer/PHPMailer)
- [Symfony Mailer](https://symfony.com/doc/current/components/mailer.html)

onelinerhub: [How do I decide between using PHPMailer and Symfony Mailer for sending emails?](https://onelinerhub.com/phpmailer/how-do-i-decide-between-using-phpmailer-and-symfony-mailer-for-sending-emails)