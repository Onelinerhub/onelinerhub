# How to disable delivery in Swiftmailer?
// plain

Swiftmailer is a popular library for sending emails in PHP. To disable delivery in Swiftmailer, you can set the `disable_delivery` option to `true` in the configuration array.

```php
$transport = Swift_SmtpTransport::newInstance('smtp.example.org', 25)
    ->setUsername('your username')
    ->setPassword('your password')
    ->setDisableDelivery(true);
```

This will prevent emails from being sent when using the transport.

## Code explanation


- `Swift_SmtpTransport::newInstance()`: Creates a new instance of the SMTP transport.
- `->setUsername()`: Sets the username for authentication.
- `->setPassword()`: Sets the password for authentication.
- `->setDisableDelivery()`: Sets the `disable_delivery` option to `true` in the configuration array.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to disable delivery in Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-disable-delivery-in-swiftmailer)