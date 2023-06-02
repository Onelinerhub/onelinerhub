# How do I fix PHPMailer when it's not working?
// plain

1. First, check the SMTP settings for your PHPMailer instance. Ensure that the host, port, username, password, and authentication method are all correct.

2. Next, make sure that the email address you are sending from is valid and that the domain is valid.

3. If you are using a third-party SMTP service, such as Gmail, make sure that you have enabled less secure apps in the account settings.

4. If you are using a local SMTP server, make sure it is configured correctly and is running properly.

5. If you are using a local mail server, make sure that it is configured to accept emails from your domain.

6. Make sure that the email address you are sending to is valid and that the domain is valid.

7. Check your PHP error log for any errors related to PHPMailer.

Example Code Block:

```
$mail = new PHPMailer;
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->Port = 465;
$mail->SMTPAuth = true;
$mail->Username = 'user@example.com';
$mail->Password = 'password';
$mail->setFrom('from@example.com', 'Mailer');
$mail->addAddress('joe@example.net', 'Joe User');
$mail->Subject = 'Here is the subject';
$mail->Body    = 'This is the HTML message body <b>in bold!</b>';
$mail->send();
```

Output (if any):

No output.

onelinerhub: [How do I fix PHPMailer when it's not working?](https://onelinerhub.com/phpmailer/how-do-i-fix-phpmailer-when-it-s-not-working)