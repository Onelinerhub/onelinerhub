# How do I configure PHPMailer to use Outlook's SMTP server?
// plain

1. First, install the PHPMailer library:
   ```
   composer require phpmailer/phpmailer
   ```

2. Next, create a new instance of the PHPMailer class:
   ```php
   $mail = new PHPMailer;
   ```

3. Then, configure the SMTP settings for Outlook:
   ```php
   $mail->isSMTP();
   $mail->Host = 'smtp-mail.outlook.com';
   $mail->SMTPAuth = true;
   $mail->Username = 'your_outlook_username';
   $mail->Password = 'your_outlook_password';
   $mail->SMTPSecure = 'tls';
   $mail->Port = 587;
   ```

4. Then, set the from address and other message properties:
   ```php
   $mail->setFrom('from@example.com', 'Your Name');
   $mail->addAddress('to@example.com', 'Receipient Name');
   $mail->Subject = 'PHPMailer Outlook Test';
   $mail->Body    = 'This is a test message sent with PHPMailer using Outlook\'s SMTP server.';
   ```

5. Finally, send the message:
   ```php
   if(!$mail->send()) {
       echo 'Message could not be sent.';
       echo 'Mailer Error: ' . $mail->ErrorInfo;
   } else {
       echo 'Message has been sent';
   }
   ```

6. If successful, the output should look like this:
   ```
   Message has been sent
   ```

7. For more information, please refer to the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki/Using-Gmail-or-Outlook-with-PHPMailer).

onelinerhub: [How do I configure PHPMailer to use Outlook's SMTP server?](https://onelinerhub.com/phpmailer/how-do-i-configure-phpmailer-to-use-outlook-s-smtp-server)