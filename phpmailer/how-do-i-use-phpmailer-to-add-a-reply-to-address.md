# How do I use PHPMailer to add a reply-to address?
// plain

You can use PHPMailer to add a reply-to address in the following way:

1. Include the PHPMailer library in your project:
```
require 'path/to/PHPMailer/src/PHPMailer.php';
```

2. Create a new instance of the `PHPMailer` class:
```php
$mail = new PHPMailer;
```

3. Set the `addReplyTo` method to add the reply-to address:
```php
$mail->addReplyTo('reply@example.com', 'Reply Name');
```

4. Send the email as usual:
```php
$mail->send();
```

The `addReplyTo` method takes two parameters: an email address and the name of the recipient.

You can find more information about PHPMailer and its `addReplyTo` method in the [official documentation](https://github.com/PHPMailer/PHPMailer/blob/master/docs/MAIL.md).

onelinerhub: [How do I use PHPMailer to add a reply-to address?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-add-a-reply-to-address)