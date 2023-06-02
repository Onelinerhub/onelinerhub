# How do I configure PHPMailer to work with cPanel?
// plain

1. Download the latest version of PHPMailer from [GitHub](https://github.com/PHPMailer/PHPMailer).
2. Extract the files into the directory of your choice.
3. Create a new file to hold your code and include the PHPMailer library:
```
<?php
require 'path/to/PHPMailer/src/PHPMailer.php';
require 'path/to/PHPMailer/src/SMTP.php';
```
4. Create a new PHPMailer object and set the SMTP authentication details:
```
<?php
$mail = new PHPMailer;
$mail->isSMTP();
$mail->Host = 'your_cPanel_hostname';
$mail->SMTPAuth = true;
$mail->Username = 'your_cPanel_username';
$mail->Password = 'your_cPanel_password';
$mail->SMTPSecure = 'tls';
$mail->Port = 587;
```
5. Set the email details and send the message:
```
<?php
$mail->setFrom('from@example.com', 'From Name');
$mail->addAddress('to@example.com', 'To Name');
$mail->Subject = 'PHPMailer cPanel Test';
$mail->Body = 'This is a test message using PHPMailer and cPanel.';

if (!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
```

6. To test, run the script. If successful, you should see the output `Message has been sent`.
7. For more information, see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/blob/master/docs/README.md).

onelinerhub: [How do I configure PHPMailer to work with cPanel?](https://onelinerhub.com/phpmailer/how-do-i-configure-phpmailer-to-work-with-cpanel)