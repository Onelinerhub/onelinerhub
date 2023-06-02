# How do I use a CDN with PHPMailer?
// plain

Using a CDN with PHPMailer is a great way to improve the speed and performance of your email delivery. To do this, you need to include a CDN URL for PHPMailer in your code.

For example, if you are using Cloudflare's CDN, you can add the following code to your PHP script:
```
require 'https://cdnjs.cloudflare.com/ajax/libs/phpmailer/6.1.7/class.phpmailer.php';
```

This code will include the PHPMailer library from Cloudflare's CDN, allowing you to send emails using PHPMailer without having to download and install the library.

You can then use the PHPMailer library to send emails, such as the following example:
```
$mail = new PHPMailer();
$mail->setFrom('example@example.com', 'Example');
$mail->addAddress('recipient@example.com', 'Recipient');
$mail->Subject = 'Example PHPMailer Email';
$mail->Body = 'This is an example PHPMailer email.';
$mail->send();
```

This code will create a new PHPMailer object, set the sender and recipient addresses, set the subject and body of the email, and then send the email.

## Helpful links
- [Cloudflare CDN](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/)
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer)

onelinerhub: [How do I use a CDN with PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-use-a-cdn-with-phpmailer)