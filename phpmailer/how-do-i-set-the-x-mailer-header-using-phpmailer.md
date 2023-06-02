# How do I set the X-Mailer header using PHPMailer?
// plain

The X-Mailer header can be set using PHPMailer by using the `addCustomHeader()` method. The following example code block sets the X-Mailer header to `MyXMailer`:

```php
<?php
// Include PHPMailer library
require_once('PHPMailer/PHPMailerAutoload.php');

// Create new PHPMailer instance
$mail = new PHPMailer;

// Set X-Mailer header
$mail->addCustomHeader('X-Mailer', 'MyXMailer');

// ...

?>
```

The `addCustomHeader()` method takes two parameters: the header name and header value. The header name is the name of the header, in this case `X-Mailer`, and the header value is the value of the header, in this case `MyXMailer`.

The following list explains the parts of the code example:

- `require_once('PHPMailer/PHPMailerAutoload.php');`: This line includes the PHPMailer library.
- `$mail = new PHPMailer;`: This line creates a new PHPMailer instance.
- `$mail->addCustomHeader('X-Mailer', 'MyXMailer');`: This line sets the X-Mailer header to `MyXMailer`.

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/blob/master/docs/README.md)
- [addCustomHeader() Method](https://github.com/PHPMailer/PHPMailer/blob/master/docs/classes/PHPMailer.html#method_addcustomheader)

onelinerhub: [How do I set the X-Mailer header using PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-set-the-x-mailer-header-using-phpmailer)