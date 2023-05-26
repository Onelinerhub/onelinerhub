# How to encrypt emails with SwiftMailer?
// plain

SwiftMailer is a popular library for sending emails in PHP. It supports encryption of emails using the Transport Layer Security (TLS) protocol. To encrypt emails with SwiftMailer, you need to set the encryption type to "tls" when creating the transport instance.

## Example code

```php
$transport = (new Swift_SmtpTransport('smtp.example.com', 465, 'tls'))
  ->setUsername('your username')
  ->setPassword('your password');
```

The code above creates a transport instance with the encryption type set to "tls".

## Code explanation

- `Swift_SmtpTransport`: creates a transport instance for sending emails via SMTP
- `smtp.example.com`: the SMTP server address
- `465`: the SMTP port
- `tls`: the encryption type
- `setUsername`: sets the username for authentication
- `setPassword`: sets the password for authentication

## Helpful links
- [SwiftMailer documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [SwiftMailer encryption](https://swiftmailer.symfony.com/docs/sending.html#encryption)

onelinerhub: [How to encrypt emails with SwiftMailer?](https://onelinerhub.com/php-swiftmailer/how-to-encrypt-emails-with-swiftmailer)