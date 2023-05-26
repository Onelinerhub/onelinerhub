# How to enable StartTLS with Swiftmailer?
// plain

Swiftmailer supports StartTLS for secure connections. To enable StartTLS with Swiftmailer, you need to set the encryption option to `tls` when creating the transport instance.

```php
$transport = (new Swift_SmtpTransport('smtp.example.org', 25))
  ->setEncryption('tls')
;
```

The code above will create a transport instance with StartTLS enabled.

## Code explanation


- `Swift_SmtpTransport`: Creates a transport instance for SMTP.
- `smtp.example.org`: The hostname of the SMTP server.
- `25`: The port of the SMTP server.
- `setEncryption('tls')`: Enables StartTLS with the transport instance.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to enable StartTLS with Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-enable-starttls-with-swiftmailer)