# How can I get PHPMailer to send emails to Gmail?
// plain

PHPMailer is a popular open-source library used to send emails with PHP. To send emails to Gmail, you need to configure the PHPMailer object with the correct SMTP settings.

Here's an example code block to send an email to Gmail using PHPMailer:

```php
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
    $mail->Host       = 'smtp.gmail.com';  // Specify main and backup SMTP servers
    $mail->SMTPAuth   = true;                                   // Enable SMTP authentication
    $mail->Username   = 'your-gmail-username@gmail.com';                     // SMTP username
    $mail->Password   = 'your-gmail-password';                               // SMTP password
    $mail->SMTPSecure = 'tls';                                  // Enable TLS encryption, `ssl` also accepted
    $mail->Port       = 587;                                    // TCP port to connect to

    //Recipients
    $mail->setFrom('from@example.com', 'Mailer');
    $mail->addAddress('your-gmail-username@gmail.com', 'Joe User');     // Add a recipient

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

## Code explanation


1. Import PHPMailer classes - `use PHPMailer\PHPMailer\PHPMailer;` and `use PHPMailer\PHPMailer\Exception;`
2. Load Composer's autoloader - `require 'vendor/autoload.php';`
3. Instantiate PHPMailer object - `$mail = new PHPMailer(true);`
4. Configure SMTP settings - `$mail->SMTPDebug = 0;`, `$mail->isSMTP();`, `$mail->Host = 'smtp.gmail.com';`, `$mail->SMTPAuth = true;`, `$mail->Username = 'your-gmail-username@gmail.com';`, `$mail->Password = 'your-gmail-password';`, `$mail->SMTPSecure = 'tls';` and `$mail->Port = 587;`
5. Set recipient and sender - `$mail->setFrom('from@example.com', 'Mailer');` and `$mail->addAddress('your-gmail-username@gmail.com', 'Joe User');`
6. Set email content - `$mail->isHTML(true);` and `$mail->Subject = 'Here is the subject';` and `$mail->Body = 'This is the HTML message body <b>in bold!</b>';`
7. Send email - `$mail->send();`

If the email was sent successfully, the output of the code should be `Message has been sent`.

For more information, please refer to the [official PHPMailer documentation](https://github.com/PHPMailer/PHPMailer).

onelinerhub: [How can I get PHPMailer to send emails to Gmail?](https://onelinerhub.com/phpmailer/how-can-i-get-phpmailer-to-send-emails-to-gmail)