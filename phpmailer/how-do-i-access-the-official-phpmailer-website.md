# How do I access the official PHPMailer website?
// plain

The official PHPMailer website can be accessed at [https://github.com/PHPMailer/PHPMailer](https://github.com/PHPMailer/PHPMailer).

The website contains all the information you need to get started with PHPMailer, including documentation, examples, and support resources.

To install PHPMailer, you can use the following code:
```
composer require phpmailer/phpmailer
```

This will install the latest version of PHPMailer.

To send an email using PHPMailer, you can use the following code:
```php
<?php
// Import the PHPMailer class into the global namespace
use PHPMailer\PHPMailer\PHPMailer;

// Create a new PHPMailer instance
$mail = new PHPMailer;

// Set a sender
$mail->setFrom('from@example.com', 'Mailer');

// Set a recipient
$mail->addAddress('to@example.com', 'John Doe');

// Set the subject
$mail->Subject = 'PHPMailer Test';

// Set the body of the message
$mail->Body = 'This is a test using PHPMailer';

// Send the message
$mail->send();
```

The website also provides additional resources, such as tutorials, FAQs, and troubleshooting guides. Additionally, there is an active community forum where you can ask questions and get help from the PHPMailer team and other users.

onelinerhub: [How do I access the official PHPMailer website?](https://onelinerhub.com/phpmailer/how-do-i-access-the-official-phpmailer-website)