# How do I configure the timeout settings for PHPMailer?
// plain

PHPMailer provides a lot of options to configure the timeout settings, such as:

1. `Timeout`: This is the timeout value for the socket connection. The default value is `30` seconds. This can be configured as follows:

```
$mail->Timeout=60;
```

2. `SMTPOptions`: This is an array of options for the underlying stream_context_create() call. It provides options for the stream_context, such as the timeout value. The default value is `30` seconds. This can be configured as follows:

```
$mail->SMTPOptions = array(
    'ssl' => array(
        'verify_peer' => false,
        'verify_peer_name' => false,
        'allow_self_signed' => true
    ),
    'timeout' => 60
);
```

3. `SMTPDebug`: This is the debug output level. It can be set to `1` for simple debugging, or `2` to show more verbose debugging. The default value is `0` (no debugging). This can be configured as follows:

```
$mail->SMTPDebug = 2;
```

These options can be used to configure the timeout settings for PHPMailer.

## Helpful links

- [PHPMailer Documentation](https://github.com/PHPMailer/PHPMailer/wiki/Tutorial)
- [PHPMailer API Reference](https://github.com/PHPMailer/PHPMailer/wiki/API)

onelinerhub: [How do I configure the timeout settings for PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-configure-the-timeout-settings-for-phpmailer)