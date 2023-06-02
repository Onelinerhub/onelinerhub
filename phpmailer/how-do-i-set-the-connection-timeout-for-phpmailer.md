# How do I set the connection timeout for PHPMailer?
// plain

The connection timeout for PHPMailer can be set using the `Timeout` property. This property takes an integer that sets the timeout in seconds.

For example, to set the timeout to 5 seconds, the code would be:
```
$mail->Timeout = 5;
```

The connection timeout can also be set using the `SMTPOptions` property. This property takes an array of options which can include a timeout setting.

For example, to set the timeout to 10 seconds, the code would be:
```
$mail->SMTPOptions = array(
    'ssl' => array(
        'verify_peer' => false,
        'verify_peer_name' => false,
        'allow_self_signed' => true
    ),
    'timeout' => 10
);
```

The parts of the code are:
- `$mail`: The PHPMailer instance
- `Timeout`: The property used to set the timeout in seconds
- `SMTPOptions`: The property used to set an array of options, including the timeout
- `ssl`: An array of SSL options
- `verify_peer`: A boolean option to verify the peer's SSL certificate
- `verify_peer_name`: A boolean option to verify the peer's name
- `allow_self_signed`: A boolean option to allow self-signed certificates
- `timeout`: An integer option to set the timeout in seconds

## Helpful links
- [GitHub - PHPMailer/PHPMailer: A full-featured email creation and transfer class for PHP](https://github.com/PHPMailer/PHPMailer)
- [How to Set SMTP Options with PHPMailer - ServerPilot](https://serverpilot.io/community/articles/how-to-set-smtp-options-with-phpmailer.html)

onelinerhub: [How do I set the connection timeout for PHPMailer?](https://onelinerhub.com/phpmailer/how-do-i-set-the-connection-timeout-for-phpmailer)