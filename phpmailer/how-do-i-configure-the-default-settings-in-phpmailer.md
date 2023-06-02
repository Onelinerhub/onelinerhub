# How do I configure the default settings in PHPMailer?
// plain

PHPMailer is an open source library for sending emails from PHP applications. It can be configured to use the default settings for sending emails.

The following code example shows how to configure the default settings for PHPMailer:
```
<?php
// Include the PHPMailer library
require_once('PHPMailerAutoload.php');

// Create a new PHPMailer object
$mail = new PHPMailer;

// Set default settings
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'username';
$mail->Password = 'password';
$mail->SMTPSecure = 'tls';
$mail->Port = 587;
```

The settings above will configure PHPMailer to use SMTP for sending emails. The `Host` setting specifies the SMTP server to be used. The `Username` and `Password` settings are used for authentication. The `SMTPSecure` setting specifies the type of encryption to be used for the connection. The `Port` setting specifies the port to be used.

For more information on configuring PHPMailer, please refer to the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki).

onelinerhub: [How do I configure the default settings in PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-configure-the-default-settings-in-phpmailer)