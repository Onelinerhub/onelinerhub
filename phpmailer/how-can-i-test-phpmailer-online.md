# How can I test PHPMailer online?
// plain

Testing PHPMailer online requires a few steps.

1. Create a basic HTML form with a submit button. This form should have an email field and a message field.

```
<form action="send.php" method="post">
  Email: <input type="text" name="email"><br>
  Message: <input type="text" name="message"><br>
  <input type="submit" value="Submit">
</form>
```

2. Create a PHP script that will contain the PHPMailer code. This script should include the necessary configuration for the mail server, and should have the code to send the email.

```
<?php
require 'PHPMailerAutoload.php';

$mail = new PHPMailer;

//Server settings
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'user@example.com';
$mail->Password = 'secret';

//Recipients
$mail->setFrom('from@example.com', 'Mailer');
$mail->addAddress($_POST['email'], 'User');

//Content
$mail->isHTML(true);
$mail->Subject = 'Here is the subject';
$mail->Body    = $_POST['message'];

if(!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
?>
```

3. Upload the HTML form and the PHP script to a web server.

4. Open the HTML form in a web browser, fill out the form, and submit it.

5. Check the output of the PHP script to see if the email was sent successfully.

```
Message has been sent
```

For more information, see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer).

onelinerhub: [How can I test PHPMailer online?](https://onelinerhub.com/phpmailer/how-can-i-test-phpmailer-online)