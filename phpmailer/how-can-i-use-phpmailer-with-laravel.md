# How can I use PHPMailer with Laravel?
// plain

PHPMailer is a popular library for sending emails from PHP. It can be used with Laravel to send emails from your application.

To use PHPMailer with Laravel, you need to install the package via Composer:

```
composer require phpmailer/phpmailer
```

Once installed, you can use the PHPMailer class in your controllers or services to send emails. For example, this code will send a simple email:

```
use PHPMailer\PHPMailer\PHPMailer;

$mail = new PHPMailer;

//Recipients
$mail->setFrom('from@example.com', 'Mailer');
$mail->addAddress('to@example.com', 'John Doe');

//Content
$mail->Subject = 'Here is the subject';
$mail->Body    = 'This is the HTML message body <b>in bold!</b>';

$mail->send();
```

The code above will send an email with the subject "Here is the subject" and the body "This is the HTML message body in bold!" to the address "to@example.com" from the address "from@example.com".

You can also customize the mailer with different settings, such as setting the SMTP host and port, setting authentication, setting encryption, adding attachments, etc.

Here are some relevant links for further information:

- [PHPMailer GitHub page](https://github.com/PHPMailer/PHPMailer)
- [Laravel Documentation - Sending Mail](https://laravel.com/docs/7.x/mail)
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial)

onelinerhub: [How can I use PHPMailer with Laravel?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-with-laravel)