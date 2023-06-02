# How do I set up PHPMailer with XAMPP?
// plain

1. Download [PHPMailer](https://github.com/PHPMailer/PHPMailer) library and extract it.
2. Copy the `src` folder to the `php` directory of your XAMPP installation.
3. Create a new file in `htdocs` of your XAMPP installation and name it `mail.php`.
4. Add the following code to `mail.php`:
```php
<?php
require 'php/PHPMailer/PHPMailerAutoload.php';

$mail = new PHPMailer;

//Server settings
$mail->SMTPDebug = 3;                               // Enable verbose debug output
$mail->isSMTP();                                    // Set mailer to use SMTP
$mail->Host = 'smtp1.example.com;smtp2.example.com'; // Specify main and backup SMTP servers
$mail->SMTPAuth = true;                             // Enable SMTP authentication
$mail->Username = 'user@example.com';               // SMTP username
$mail->Password = 'secret';                         // SMTP password
$mail->SMTPSecure = 'tls';                          // Enable TLS encryption, `ssl` also accepted
$mail->Port = 587;                                  // TCP port to connect to

//Recipients
$mail->setFrom('from@example.com', 'Mailer');
$mail->addAddress('joe@example.net', 'Joe User');    // Add a recipient
$mail->addAddress('ellen@example.com');             // Name is optional
$mail->addReplyTo('info@example.com', 'Information');
$mail->addCC('cc@example.com');
$mail->addBCC('bcc@example.com');

//Attachments
$mail->addAttachment('/var/tmp/file.tar.gz');        // Add attachments
$mail->addAttachment('/tmp/image.jpg', 'new.jpg');   // Optional name

//Content
$mail->isHTML(true);                                 // Set email format to HTML
$mail->Subject = 'Here is the subject';
$mail->Body    = 'This is the HTML message body <b>in bold!</b>';
$mail->AltBody = 'This is the body in plain text for non-HTML mail clients';

if(!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
```
5. Run `mail.php` in your browser.
6. Check the output of the code. It should look like this:
```
Message has been sent
```
7. Now you have successfully set up PHPMailer with XAMPP!

onelinerhub: [How do I set up PHPMailer with XAMPP?](https://onelinerhub.com/phpmailer/how-do-i-set-up-phpmailer-with-xampp)