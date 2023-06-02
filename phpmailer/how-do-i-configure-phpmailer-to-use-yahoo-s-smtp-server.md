# How do I configure PHPMailer to use Yahoo's SMTP server?
// plain

To configure PHPMailer to use Yahoo's SMTP server, you need to specify the SMTP host, port, authentication type, and the username and password of your Yahoo account.

## Example code

```
require 'PHPMailerAutoload.php';

$mail = new PHPMailer;

// Specify main and backup SMTP servers
$mail->SMTPAuth = true;                               // Enable SMTP authentication
$mail->SMTPSecure = 'tls';                            // Enable TLS encryption, `ssl` also accepted
$mail->Host = 'smtp.mail.yahoo.com';                  // Specify main and backup SMTP servers
$mail->Port = 587;                                    // TCP port to connect to
$mail->Username = 'example@yahoo.com';                 // SMTP username
$mail->Password = 'your_password';                    // SMTP password
```

No output from this example code.

## Code explanation

- `require 'PHPMailerAutoload.php'`: This line is required to access the PHPMailer class.
- `$mail = new PHPMailer;`: This line creates a PHPMailer object.
- `$mail->SMTPAuth = true;`: This line enables SMTP authentication.
- `$mail->SMTPSecure = 'tls';`: This line enables TLS encryption.
- `$mail->Host = 'smtp.mail.yahoo.com';`: This line specifies the SMTP host, which is `smtp.mail.yahoo.com` for Yahoo's SMTP server.
- `$mail->Port = 587;`: This line specifies the SMTP port, which is 587 for Yahoo's SMTP server.
- `$mail->Username = 'example@yahoo.com';`: This line sets the SMTP username, which is your Yahoo email address.
- `$mail->Password = 'your_password';`: This line sets the SMTP password, which is your Yahoo account password.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [Yahoo SMTP Server Settings](https://help.yahoo.com/kb/SLN7253.html)

onelinerhub: [How do I configure PHPMailer to use Yahoo's SMTP server?](https://onelinerhub.com/phpmailer/how-do-i-configure-phpmailer-to-use-yahoo-s-smtp-server)