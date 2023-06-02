# How do I view the log for my PHPMailer emails?
// plain

To view the log for PHPMailer emails, you can use the `$mail->SMTPDebug` property. This property can be set to one of four values: 0 (no output), 1 (errors and messages), 2 (messages only), or 3 (verbose debug output).

For example, to view verbose debug output, you can use the following code:

```php
<?php
require 'PHPMailerAutoload.php';

$mail = new PHPMailer;
$mail->SMTPDebug = 3;

// other settings

$mail->send();
echo "Message sent!";
?>
```

This will output something like the following:

```
SERVER -> CLIENT: 220 smtp.example.com ESMTP Postfix
CLIENT -> SERVER: EHLO localhost
SERVER -> CLIENT: 250-smtp.example.com
SERVER -> CLIENT: 250-PIPELINING
SERVER -> CLIENT: 250-SIZE 10240000
SERVER -> CLIENT: 250-VRFY
SERVER -> CLIENT: 250-ETRN
SERVER -> CLIENT: 250-STARTTLS
SERVER -> CLIENT: 250-ENHANCEDSTATUSCODES
SERVER -> CLIENT: 250-8BITMIME
SERVER -> CLIENT: 250 DSN
```

The `$mail->SMTPDebug` property is set to `3` by default. It can be set to any of the four values before the `$mail->send()` method is called.

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/blob/master/docs/README.md)
- [SMTPDebug Property Documentation](https://github.com/PHPMailer/PHPMailer/blob/master/docs/debugging.md#smtpdebug)

onelinerhub: [How do I view the log for my PHPMailer emails?](https://onelinerhub.com/phpmailer/how-do-i-view-the-log-for-my-phpmailer-emails)