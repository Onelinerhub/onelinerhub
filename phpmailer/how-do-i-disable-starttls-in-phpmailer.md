# How do I disable STARTTLS in PHPMailer?
// plain

To disable STARTTLS in PHPMailer, you need to set `SMTPSecure` to `false` and `SMTPAutoTLS` to `false` in your mailer configuration.

## Example code

```
$mail = new PHPMailer;
$mail->SMTPSecure = false;
$mail->SMTPAutoTLS = false;
```

These two settings will disable the STARTTLS encryption in PHPMailer.

## Code explanation

* `SMTPSecure` - This setting is used to set the encryption type of the connection. Setting it to `false` will disable encryption.
* `SMTPAutoTLS` - This setting is used to enable or disable TLS encryption automatically. Setting it to `false` will disable it.

## Helpful links
* [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)

onelinerhub: [How do I disable STARTTLS in PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-disable-starttls-in-phpmailer)