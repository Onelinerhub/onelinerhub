# How do I set the return path in PHPMailer?
// plain

The return path is the email address that will receive the bounced emails. To set the return path in PHPMailer, you can use the `addCustomHeader()` method.

```
$mail->addCustomHeader('Return-Path', 'bounce@example.com');
```

This will set the return path to `bounce@example.com`.

Parts of the code:

* `addCustomHeader()` - a method to add a custom header to the email
* `Return-Path` - the header name
* `bounce@example.com` - the email address to receive the bounced emails

## Helpful links

* [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer)
* [PHPMailer examples](https://github.com/PHPMailer/PHPMailer/tree/master/examples)

onelinerhub: [How do I set the return path in PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-set-the-return-path-in-phpmailer)