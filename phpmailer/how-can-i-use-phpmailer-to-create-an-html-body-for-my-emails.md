# How can I use PHPMailer to create an HTML body for my emails?
// plain

Using PHPMailer to create an HTML body for emails is quite simple. The example code below shows how to set the body of an email to HTML using PHPMailer:

```php
$mail = new PHPMailer;
$mail->isHTML(true);
$mail->Body = '<h1>Hello World!</h1><p>This is an HTML email.</p>';
```

The code above creates a new PHPMailer instance, sets the `isHTML` property to true, and sets the `Body` property to an HTML string.

The parts of the code above are:

1. `$mail = new PHPMailer;` - creates a new PHPMailer instance.
2. `$mail->isHTML(true);` - sets the `isHTML` property to true, indicating that the body of the email should be treated as HTML.
3. `$mail->Body = '<h1>Hello World!</h1><p>This is an HTML email.</p>';` - sets the `Body` property to an HTML string.

For more information on using PHPMailer to create HTML emails, see the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial).

onelinerhub: [How can I use PHPMailer to create an HTML body for my emails?](https://onelinerhub.com/phpmailer/how-can-i-use-phpmailer-to-create-an-html-body-for-my-emails)