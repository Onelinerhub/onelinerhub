# How can I use PHPMailer to send emails from my WordPress site?
// plain

PHPMailer is a library for sending emails from PHP applications. It can be used with WordPress sites to send emails from the site. To use PHPMailer with WordPress, you will need to include the library in your project and call it from the functions.php file. Here is an example of code that can be used to send an email with PHPMailer in WordPress:

```
<?php
// Include the PHPMailer library
require_once('path/to/PHPMailer/class.phpmailer.php');

// Create a new PHPMailer object
$mail = new PHPMailer();

// Set the From address
$mail->From = 'my@email.com';

// Set the To address
$mail->AddAddress('recipient@email.com');

// Set the Subject
$mail->Subject = 'This is a test email';

// Set the body of the message
$mail->Body = 'This is a test email sent with PHPMailer in WordPress.';

// Send the email
$mail->Send();
```

This code will send an email with the specified subject and body text. The `$mail` object is used to set the From address, To address, Subject, and Body of the email. The `$mail->Send()` method is used to actually send the email.

## Code explanation


- `require_once('path/to/PHPMailer/class.phpmailer.php')`: This line includes the PHPMailer library in the project.
- `$mail = new PHPMailer()`: This line creates a new PHPMailer object.
- `$mail->From = 'my@email.com'`: This line sets the From address of the email.
- `$mail->AddAddress('recipient@email.com')`: This line sets the To address of the email.
- `$mail->Subject = 'This is a test email'`: This line sets the Subject of the email.
- `$mail->Body = 'This is a test email sent with PHPMailer in WordPress.'`: This line sets the body of the email.
- `$mail->Send()`: This line sends the email.

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)
- [WordPress Documentation](https://wordpress.org/support/article/wordpress-emails/)

onelinerhub: [How can I use PHPMailer to send emails from my WordPress site?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-to-send-emails-from-my-wordpress-site)