# How do I use PHPMailer to verify a peer?
// plain

PHPMailer is a popular open source library for sending emails using PHP. To verify a peer with PHPMailer, you can use the SMTP authentication feature. This will require the peer to provide a valid username and password in order to send an email. Here is an example of how to use this feature:

```php
$mail = new PHPMailer();
$mail->SMTPAuth = true;
$mail->Username = "example@example.com";
$mail->Password = "examplepassword";
$mail->Send();
```

This code will attempt to authenticate the user with the provided username and password. If successful, the email will be sent.

## Code explanation


1. `$mail = new PHPMailer();` - This creates a new instance of PHPMailer.
2. `$mail->SMTPAuth = true;` - This enables SMTP authentication.
3. `$mail->Username = "example@example.com";` - This sets the username to be used for authentication.
4. `$mail->Password = "examplepassword";` - This sets the password to be used for authentication.
5. `$mail->Send();` - This sends the email.

For more information on using PHPMailer to verify a peer, see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial).

onelinerhub: [How do I use PHPMailer to verify a peer?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-verify-a-peer)