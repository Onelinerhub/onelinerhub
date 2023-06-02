# How do I configure PHPMailer to use SSL?
// plain

To configure PHPMailer to use SSL, you need to set the `SMTPSecure` property to `'ssl'` and the `Port` property to `465`. Then, you need to call the `setSMTPOptions()` method to set the `ssl` option to `true` and the `tls` option to `false`. For example:

```php
$mail->SMTPSecure = 'ssl';
$mail->Port = 465;
$mail->setSMTPOptions(array(
    'ssl' => array(
        'verify_peer' => false,
        'verify_peer_name' => false,
        'allow_self_signed' => true
    ),
    'tls' => false
));
```

Additionally, you may need to set the `Host` property to `ssl://smtp.example.com` if your mail server requires it.

- `SMTPSecure` property to `'ssl'`: sets the connection to use SSL.
- `Port` property to `465`: sets the port to use for SSL connections.
- `setSMTPOptions()` method: sets the `ssl` and `tls` options for the connection.
- `Host` property to `ssl://smtp.example.com`: sets the mail server to use for SSL connections.

## Helpful links
- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)
- [Using SMTP Authentication](https://github.com/PHPMailer/PHPMailer/wiki/Using-SMTP-Authentication)

onelinerhub: [How do I configure PHPMailer to use SSL?](https://onelinerhub.com/phpmailer/how-do-i-configure-phpmailer-to-use-ssl)