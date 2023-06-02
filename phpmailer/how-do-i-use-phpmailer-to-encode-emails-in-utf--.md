# How do I use PHPMailer to encode emails in UTF-8?
// plain

PHPMailer is a powerful library for sending emails with PHP. To encode emails in UTF-8, you can use the `setCharset` method of the `PHPMailer` class.

## Example code

```php
<?php
require 'PHPMailerAutoload.php';

$mail = new PHPMailer;
$mail->CharSet = 'UTF-8';

// ...

?>
```

The code above sets the character set of the PHPMailer instance to UTF-8. This will ensure that the emails sent through PHPMailer are encoded in UTF-8.

## Code explanation


1. `require 'PHPMailerAutoload.php';`: This line imports the PHPMailer library.
2. `$mail = new PHPMailer;`: This line creates a new instance of the PHPMailer class.
3. `$mail->CharSet = 'UTF-8';`: This line sets the character set of the PHPMailer instance to UTF-8.

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)

onelinerhub: [How do I use PHPMailer to encode emails in UTF-8?](https://onelinerhub.com/phpmailer/how-do-i-use-phpmailer-to-encode-emails-in-utf--)