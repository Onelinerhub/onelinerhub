# How do I configure PHPMailer to use a proxy?
// plain

PHPMailer can be configured to use a proxy by setting the `SMTPOptions` property of the `PHPMailer` class instance to an array containing the proxy settings. The example below shows how to configure PHPMailer to use an SOCKS5 proxy.

```php
$mail = new PHPMailer;
$mail->SMTPOptions = array(
    'ssl' => array(
        'verify_peer' => false,
        'verify_peer_name' => false,
        'allow_self_signed' => true
    ),
    'socks' => array(
        'host' => 'socks.example.com',
        'port' => '1080',
        'username' => 'username',
        'password' => 'password'
    )
);
```

The code above sets the following properties:

* `ssl`: An array containing settings for SSL/TLS connection.
    * `verify_peer`: Set to `false` to disable peer verification.
    * `verify_peer_name`: Set to `false` to disable peer name verification.
    * `allow_self_signed`: Set to `true` to allow self-signed certificates.
* `socks`: An array containing settings for the SOCKS5 proxy.
    * `host`: The hostname or IP address of the SOCKS5 proxy.
    * `port`: The port of the SOCKS5 proxy.
    * `username`: The username for the SOCKS5 proxy (optional).
    * `password`: The password for the SOCKS5 proxy (optional).

For more information, please refer to the [PHPMailer documentation](https://github.com/PHPMailer/PHPMailer/wiki/Using-SMTP-Proxies).

onelinerhub: [How do I configure PHPMailer to use a proxy?](https://onelinerhub.com/phpmailer/how-do-i-configure-phpmailer-to-use-a-proxy)