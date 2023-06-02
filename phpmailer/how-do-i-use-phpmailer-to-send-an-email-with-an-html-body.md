# How do I use PHPMailer to send an email with an HTML body?
// plain

Using PHPMailer to send an email with an HTML body requires setting the `isHTML` property of the `PHPMailer` instance to `true` and then setting the `Body` property to the HTML content.

```php
<?php
require 'PHPMailerAutoload.php';

$mail = new PHPMailer;

$mail->isHTML(true);
$mail->Body = '<b>This is bold text</b>';

// ...

// send the message
$mail->send();
```

The `Body` property can also be set to the path of an HTML file, which will be read and used as the message body.

```php
<?php
require 'PHPMailerAutoload.php';

$mail = new PHPMailer;

$mail->isHTML(true);
$mail->Body = file_get_contents('path/to/message.html');

// ...

// send the message
$mail->send();
```

The content of `message.html`:

```html
<b>This is bold text</b>
```

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)
- [Example Usage of PHPMailer](https://github.com/PHPMailer/PHPMailer/blob/master/examples/mail.phps)

onelinerhub: [How do I use PHPMailer to send an email with an HTML body?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-send-an-email-with-an-html-body)