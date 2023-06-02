# How do I download PHPMailer?
// plain

PHPMailer is a popular open source library used for sending emails from PHP. It can be downloaded from [GitHub](https://github.com/PHPMailer/PHPMailer).

To install PHPMailer, you can either clone the repository using git:
```
git clone https://github.com/PHPMailer/PHPMailer.git
```
or download a release from the [Releases](https://github.com/PHPMailer/PHPMailer/releases) page.

Once the download is complete, you will need to include the `class.phpmailer.php` file in your code before you can use the library. You can do this by adding the following line:
```
require 'path/to/PHPMailer/src/PHPMailer.php';
```

You can also install PHPMailer using [Composer](https://getcomposer.org/):
```
composer require phpmailer/phpmailer
```

After installation, you can use PHPMailer to send emails in your PHP code. For example:
```
<?php
  require 'path/to/PHPMailer/src/PHPMailer.php';

  $mail = new PHPMailer();
  $mail->addAddress('user@example.com', 'User');
  $mail->Subject = 'Test Email';
  $mail->Body = 'This is a test email.';
  $mail->send();
?>
```

This code will send an email to `user@example.com` with the subject "Test Email" and the body "This is a test email."

onelinerhub: [How do I download PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-download-phpmailer)