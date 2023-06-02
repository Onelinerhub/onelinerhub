# How do I install PHPMailer?
// plain

1. Download the PHPMailer [zip file](https://github.com/PHPMailer/PHPMailer/releases/download/v6.1.7/phpmailer-6.1.7.zip) and extract it.
2. Include the PHPMailer autoloader in your script: `require 'path/to/PHPMailer/src/PHPMailerAutoload.php';`
3. Create a PHPMailer object: `$mail = new PHPMailer();`
4. Configure the mail server, sender address, recipient address, and so on:
```
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'user@example.com';
$mail->Password = 'secret';
$mail->setFrom('from@example.com', 'First Last');
$mail->addAddress('whoto@example.com', 'John Doe');
```
5. Add the content of the email:
```
$mail->isHTML(true);
$mail->Subject = 'Here is the subject';
$mail->Body    = 'This is the HTML message body <b>in bold!</b>';
```
6. Send the message: `$mail->send();`
7. Check for errors:
```
if(!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
```

## Output example

`Message has been sent`

onelinerhub: [How do I install PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-install-phpmailer)