# How to enable encryption in Swiftmailer?
// plain

Swiftmailer supports encryption through the use of Transport Layer Security (TLS) and Secure Sockets Layer (SSL). To enable encryption, you need to set the encryption option in the transport configuration.

```php
// Create the Transport
$transport = (new Swift_SmtpTransport('smtp.example.org', 25))
  ->setUsername('your username')
  ->setPassword('your password')
  ->setEncryption('tls')
;
```

The above example code will enable TLS encryption for the transport. You can also use `ssl` instead of `tls` to enable SSL encryption.

- `Swift_SmtpTransport`: Creates a new SMTP transport instance.
- `setUsername`: Sets the username to authenticate with.
- `setPassword`: Sets the password to authenticate with.
- `setEncryption`: Sets the encryption type (`tls` or `ssl`).

## Helpful links
- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [Swiftmailer Transport Configuration](https://swiftmailer.symfony.com/docs/sending.html#transport-configuration)

onelinerhub: [How to enable encryption in Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-enable-encryption-in-swiftmailer)