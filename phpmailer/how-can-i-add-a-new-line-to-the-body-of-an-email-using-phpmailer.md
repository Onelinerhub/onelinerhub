# How can I add a new line to the body of an email using PHPMailer?
// plain

Adding a new line to the body of an email using PHPMailer is a simple process. The following example code shows how to add a new line with a text message to the body of an email using PHPMailer:

```
<?php
  require 'PHPMailerAutoload.php';
  $mail = new PHPMailer();
  $mail->Body = "Hello!\nThis is a new line.";
  echo $mail->Body;
?>
```

The output of this code will be:

```
Hello!
This is a new line.
```

The code consists of the following parts:

1. The `require` statement which includes the PHPMailerAutoload.php file. This file contains the necessary code for PHPMailer to work correctly.
2. The `$mail` variable which is an instance of the `PHPMailer` class.
3. The `$mail->Body` statement which sets the body of the email.
4. The `echo` statement which prints out the body of the email.

For more information on how to use PHPMailer to send emails, see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer).

onelinerhub: [How can I add a new line to the body of an email using PHPMailer?](https://onelinerhub.com/phpmailer/how-can-i-add-a-new-line-to-the-body-of-an-email-using-phpmailer)