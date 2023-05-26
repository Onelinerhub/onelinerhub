# How to disable SSL verification in Swiftmailer?
// plain

Swiftmailer provides a way to disable SSL verification when sending emails. This can be done by setting the `verify_peer` and `verify_peer_name` options to `false` when creating the transport instance.

## Example code

```php
$transport = (new Swift_SmtpTransport('smtp.example.com', 465, 'ssl'))
    ->setUsername('your username')
    ->setPassword('your password')
    ->setStreamOptions(array('ssl' => array('verify_peer' => false, 'verify_peer_name' => false)));
```

## Code explanation

- `Swift_SmtpTransport`: Creates a new instance of the SMTP transport.
- `smtp.example.com`: The SMTP server address.
- `465`: The SMTP server port.
- `ssl`: The SMTP server encryption type.
- `setUsername`: Sets the username for authentication.
- `setPassword`: Sets the password for authentication.
- `setStreamOptions`: Sets the stream options for the transport.
- `verify_peer`: Whether to verify the peer's SSL certificate.
- `verify_peer_name`: Whether to verify the peer's name.

## Helpful links
- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to disable SSL verification in Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-disable-ssl-verification-in-swiftmailer)