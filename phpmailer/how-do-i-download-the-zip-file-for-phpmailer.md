# How do I download the zip file for PHPMailer?
// plain

1. Download the latest version of PHPMailer from the [GitHub page](https://github.com/PHPMailer/PHPMailer).
2. On the right side of the page, click the green `Clone or download` button and then click `Download ZIP`.
3. The zip file will be downloaded to your local machine.
4. Unzip the file to a directory of your choice.
5. You can now use the PHPMailer library in your project.
6. For example, you can include the PHPMailerAutoload.php file in your project to use the PHPMailer library:
```
require 'path/to/PHPMailerAutoload.php';
```
7. You can now create a PHPMailer instance and start sending emails:
```
$mail = new PHPMailer;
$mail->addAddress('example@example.com', 'John Doe');
$mail->Subject = 'PHPMailer Test';
$mail->Body    = 'This is a test email using PHPMailer.';
$mail->send();
```

onelinerhub: [How do I download the zip file for PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-download-the-zip-file-for-phpmailer)