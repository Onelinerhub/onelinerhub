# How to enable TLS with Swiftmailer?
// plain

Swiftmailer supports TLS encryption for secure communication. To enable TLS with Swiftmailer, you need to set the encryption option to `tls` in the transport configuration.

```php
$transport = (new Swift_SmtpTransport('smtp.example.org', 25))
  ->setEncryption('tls')
;
```

The code above will enable TLS encryption for the transport.

The parts of the code are:
- `Swift_SmtpTransport`: This is the transport class used to send emails via SMTP.
- `smtp.example.org`: This is the SMTP server address.
- `25`: This is the SMTP port.
- `setEncryption('tls')`: This is the method used to enable TLS encryption.

## Helpful links
- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to enable TLS with Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-enable-tls-with-swiftmailer)