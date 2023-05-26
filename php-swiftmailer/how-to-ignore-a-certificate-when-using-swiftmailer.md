# How to ignore a certificate when using Swiftmailer?
// plain

Swiftmailer provides a way to ignore a certificate when using it. To do this, you need to set the `stream_options` parameter to `['ssl' => ['verify_peer' => false, 'verify_peer_name' => false]]` when creating the transport instance.

## Example code

```php
$transport = (new Swift_SmtpTransport('smtp.example.org', 465, 'ssl'))
    ->setStreamOptions(['ssl' => ['verify_peer' => false, 'verify_peer_name' => false]]);
```

## Code explanation

- `Swift_SmtpTransport`: This is the class used to create the transport instance.
- `smtp.example.org`: This is the hostname of the SMTP server.
- `465`: This is the port used for the SMTP server.
- `ssl`: This is the encryption protocol used for the SMTP server.
- `setStreamOptions`: This is the method used to set the `stream_options` parameter.
- `['ssl' => ['verify_peer' => false, 'verify_peer_name' => false]]`: This is the value of the `stream_options` parameter, which is used to ignore the certificate.

## Helpful links
- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to ignore a certificate when using Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-ignore-a-certificate-when-using-swiftmailer)