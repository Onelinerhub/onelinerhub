# How do I use PHPMailer to embed an image in an email using Base64 encoding?
// plain

To use PHPMailer to embed an image in an email using Base64 encoding, you need to use the `addStringAttachment()` method. This method takes three parameters: the content of the attachment, the filename, and the encoding type. The content should be the Base64 encoded string of the image, the filename should be the desired name of the image, and the encoding type should be `'base64'`.

## Example code

```php
<?php

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

require 'vendor/autoload.php';

$mail = new PHPMailer(true);

$mail->isSMTP();
$mail->Host = 'smtp.gmail.com';
$mail->SMTPAuth = true;
$mail->Username = 'username@gmail.com';
$mail->Password = 'password';
$mail->SMTPSecure = 'tls';
$mail->Port = 587;

$mail->setFrom('from@example.com', 'Mailer');
$mail->addAddress('to@example.com', 'Receiver');

$mail->Subject = 'Embedded Image';
$mail->Body = 'This is an embedded image:';

$imageString = base64_encode(file_get_contents('image.jpg'));
$mail->addStringAttachment($imageString, 'image.jpg', 'base64');

$mail->send();

echo 'Message has been sent';

?>
```

## Output example

```
Message has been sent
```

## Code explanation


- `require 'vendor/autoload.php';` - This line includes the PHPMailer library.
- `$mail = new PHPMailer(true);` - This line creates a new instance of the PHPMailer class.
- `$mail->isSMTP();` - This line sets the mailer to use SMTP.
- `$mail->Host = 'smtp.gmail.com';` - This line sets the SMTP host.
- `$mail->SMTPAuth = true;` - This line sets SMTP authentication to true.
- `$mail->Username = 'username@gmail.com';` - This line sets the SMTP username.
- `$mail->Password = 'password';` - This line sets the SMTP password.
- `$mail->SMTPSecure = 'tls';` - This line sets the SMTP security type.
- `$mail->Port = 587;` - This line sets the SMTP port.
- `$mail->setFrom('from@example.com', 'Mailer');` - This line sets the from address and name.
- `$mail->addAddress('to@example.com', 'Receiver');` - This line adds the recipient address and name.
- `$mail->Subject = 'Embedded Image';` - This line sets the email subject.
- `$mail->Body = 'This is an embedded image:';` - This line sets the email body text.
- `$imageString = base64_encode(file_get_contents('image.jpg'));` - This line encodes the image in Base64.
- `$mail->addStringAttachment($imageString, 'image.jpg', 'base64');` - This line adds the image as an attachment to the email.
- `$mail->send();` - This line sends the email.

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)
- [Base64 Encode/Decode](https://www.base64encode.org/)

onelinerhub: [How do I use PHPMailer to embed an image in an email using Base64 encoding?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-embed-an-image-in-an-email-using-base---encoding)