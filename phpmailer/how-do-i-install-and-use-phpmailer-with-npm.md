# How do I install and use PHPMailer with NPM?
// plain

1. First, install the PHPMailer package from NPM with the command `npm install phpmailer`.
2. Then, create a PHP file with the following code:
```
<?php
    require 'vendor/autoload.php';

    $mail = new PHPMailer;
    // Your code here
?>
```
3. Inside the `$mail` object, configure the mail server, the sender's address, and the recipient's address. For example:
```
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'user@example.com';
$mail->Password = 'secret';
$mail->SMTPSecure = 'tls';
$mail->From = 'from@example.com';
$mail->FromName = 'Mailer';
$mail->addAddress('joe@example.net', 'Joe User');
```
4. After the mail server and addresses have been configured, add the subject, message body, and any attachments with the following commands:
```
$mail->Subject = 'Here is the subject';
$mail->Body    = 'This is the HTML message body <b>in bold!</b>';
$mail->AltBody = 'This is the body in plain text for non-HTML mail clients';
$mail->addAttachment('/var/tmp/file.tar.gz');
```
5. Finally, send the mail with `$mail->send()`, and check for errors with `$mail->ErrorInfo`.
6. You can find more information and examples in the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki).
7. Additionally, the [NPM package page](https://www.npmjs.com/package/phpmailer) has some useful information.

*Note: You should replace the example values in the code with your own.*

onelinerhub: [How do I install and use PHPMailer with NPM?](https://onelinerhub.com/phpmailer/how-do-i-install-and-use-phpmailer-with-npm)