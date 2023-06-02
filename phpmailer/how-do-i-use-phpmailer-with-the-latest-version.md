# How do I use PHPMailer with the latest version?
// plain

PHPMailer is a popular open source library for sending emails from PHP. To use it with the latest version, you need to install it via composer:

```bash
composer require phpmailer/phpmailer
```

Then, you need to include the autoloader in your script:

```php
require 'vendor/autoload.php';
```

After that, you can create a new PHPMailer instance and configure it, e.g.:

```php
$mail = new PHPMailer;
$mail->isSMTP();
$mail->Host = 'smtp.example.com';
$mail->SMTPAuth = true;
$mail->Username = 'user@example.com';
$mail->Password = 'secret';
$mail->SMTPSecure = 'tls';
$mail->Port = 587;
```

Then, you can set the email content and send it:

```php
$mail->setFrom('from@example.com', 'Mailer');
$mail->addAddress('joe@example.net', 'Joe User');
$mail->Subject = 'Here is the subject';
$mail->Body    = 'This is the HTML message body <b>in bold!</b>';

if(!$mail->send()) {
    echo 'Message could not be sent.';
    echo 'Mailer Error: ' . $mail->ErrorInfo;
} else {
    echo 'Message has been sent';
}
```

## Output example
 `Message has been sent`

## Code explanation


- `composer require phpmailer/phpmailer`: This command installs PHPMailer via composer.
- `require 'vendor/autoload.php'`: This line includes the autoloader, which is needed to load the PHPMailer classes.
- `$mail = new PHPMailer;`: This line creates a new PHPMailer instance.
- `$mail->isSMTP();`: This line configures the mailer to use SMTP.
- `$mail->Host = 'smtp.example.com';`: This line sets the SMTP host.
- `$mail->SMTPAuth = true;`: This line enables SMTP authentication.
- `$mail->Username = 'user@example.com';`: This line sets the SMTP username.
- `$mail->Password = 'secret';`: This line sets the SMTP password.
- `$mail->SMTPSecure = 'tls';`: This line sets the encryption system to use - TLS in this case.
- `$mail->Port = 587;`: This line sets the SMTP port to use.
- `$mail->setFrom('from@example.com', 'Mailer');`: This line sets the From address of the message.
- `$mail->addAddress('joe@example.net', 'Joe User');`: This line adds a recipient.
- `$mail->Subject = 'Here is the subject';`: This line sets the subject of the message.
- `$mail->Body    = 'This is the HTML message body <b>in bold!</b>';`: This line sets the HTML body of the message.
- `$mail->send()`: This line sends the message.

## Helpful links
- PHPMailer official documentation: https://github.com/PHPMailer/PHPMailer/blob/master/docs/README.md
- Composer official documentation: https://getcomposer.org/doc/

onelinerhub: [How do I use PHPMailer with the latest version?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-with-the-latest-version)