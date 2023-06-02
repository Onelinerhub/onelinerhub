# How do I use PHPMailer to send HTML emails?
// plain

PHPMailer is a library that can be used to send HTML emails. To use it, you need to include the library in your code and set up the SMTP settings.

## Example code

```
require 'PHPMailerAutoload.php';

$mail = new PHPMailer;

//Set up SMTP settings
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'username';
$mail->Password = 'password';

//Set up HTML email
$mail->Subject = 'HTML Email';
$mail->msgHTML('<h1>HTML Email</h1>');

//Send the email
$mail->send();
```

The code above sets up the SMTP settings and creates an HTML email with a heading. It then sends the email.

## Code explanation

1. `require 'PHPMailerAutoload.php'` - This line includes the PHPMailer library.
2. `$mail = new PHPMailer;` - This line creates a new instance of the PHPMailer class.
3. `$mail->isSMTP();` - This line sets the mailer to use SMTP.
4. `$mail->Host = 'smtp.example.com';` - This line sets the hostname of the SMTP server.
5. `$mail->SMTPAuth = true;` - This line sets SMTP authentication to true.
6. `$mail->Username = 'username';` - This line sets the SMTP username.
7. `$mail->Password = 'password';` - This line sets the SMTP password.
8. `$mail->Subject = 'HTML Email';` - This line sets the subject of the email.
9. `$mail->msgHTML('<h1>HTML Email</h1>');` - This line sets the body of the email to an HTML string.
10. `$mail->send();` - This line sends the email.

## Helpful links
- [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer)

onelinerhub: [How do I use PHPMailer to send HTML emails?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-send-html-emails)