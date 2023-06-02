# How do I configure PHPMailer to use TLS encryption?
// plain

To configure PHPMailer to use TLS encryption, you need to set the `SMTPSecure` property to `tls` and the `Port` property to `587` in your PHPMailer instance. You can do this as follows:

```php
$mail = new PHPMailer();
$mail->SMTPSecure = 'tls';
$mail->Port = 587;
```

You may also need to set the `SMTPOptions` property to enable TLS encryption. This should be done as follows:

```php
$mail->SMTPOptions = array(
    'ssl' => array(
        'verify_peer' => false,
        'verify_peer_name' => false,
        'allow_self_signed' => true
    )
);
```

The following are the parts of the code and their explanations:

- `SMTPSecure`: This property sets the secure connection prefix. Setting it to `tls` enables TLS encryption.
- `Port`: This property sets the SMTP port number. The port to be used for TLS encryption is 587.
- `SMTPOptions`: This property sets the SMTP options. The `ssl` array sets the `verify_peer`, `verify_peer_name` and `allow_self_signed` options, which are necessary for TLS encryption.

For more information, please refer to the [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki).

onelinerhub: [How do I configure PHPMailer to use TLS encryption?](https://onelinerhub.com/phpmailer/how-do-i-configure-phpmailer-to-use-tls-encryption)