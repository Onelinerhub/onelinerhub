# How to configure Swiftmailer for SMTP without authentication?
// plain

Swiftmailer can be configured for SMTP without authentication by setting the `transport` option to `smtp` and providing the `host`, `port` and `encryption` options.

```php
$transport = (new Swift_SmtpTransport('smtp.example.com', 25))
    ->setEncryption('tls')
    ->setTimeout(30);
```

The `host` option should be set to the SMTP server address, the `port` option should be set to the port number of the SMTP server and the `encryption` option should be set to the encryption protocol used by the SMTP server.

- `host`: SMTP server address
- `port`: port number of the SMTP server
- `encryption`: encryption protocol used by the SMTP server

## Helpful links
- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [Swiftmailer SMTP Transport](https://swiftmailer.symfony.com/docs/sending.html#smtp-transport)

onelinerhub: [How to configure Swiftmailer for SMTP without authentication?](https://onelinerhub.com/php-swiftmailer/how-to-configure-swiftmailer-for-smtp-without-authentication)