# How can I configure PHPMailer to ignore TLS certificate errors?
// plain

PHPMailer can be configured to ignore TLS certificate errors by setting the `SMTPOptions` property to an array containing the `ssl` key and the `verify_peer` and `verify_peer_name` keys set to `false` as shown in the following example:

```php
$mail->SMTPOptions = array(
    'ssl' => array(
        'verify_peer' => false,
        'verify_peer_name' => false
    )
);
```

The above code will configure PHPMailer to ignore TLS certificate errors.

## Code explanation


1. `$mail->SMTPOptions` - The property used to configure PHPMailer to ignore TLS certificate errors.
2. `ssl` - The key inside the `SMTPOptions` array that contains the settings for ignoring TLS certificate errors.
3. `verify_peer` - The key inside the `ssl` array that must be set to `false` to ignore TLS certificate errors.
4. `verify_peer_name` - The key inside the `ssl` array that must be set to `false` to ignore TLS certificate errors.

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki)

onelinerhub: [How can I configure PHPMailer to ignore TLS certificate errors?](https://onelinerhub.com/phpmailer/how-can-i-configure-phpmailer-to-ignore-tls-certificate-errors)