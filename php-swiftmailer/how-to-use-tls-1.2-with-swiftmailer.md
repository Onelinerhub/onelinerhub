# How to use TLS 1.2 with Swiftmailer?
// plain

Swiftmailer supports TLS 1.2 for secure connections. To use TLS 1.2 with Swiftmailer, you need to set the encryption option to `tls` and the `tls` option to `tlsv1.2` when creating the transport.

```php
$transport = (new Swift_SmtpTransport('smtp.example.org', 465, 'ssl'))
  ->setUsername('your username')
  ->setPassword('your password')
  ->setEncryption('tls')
  ->setStreamOptions(array('ssl' => array('allow_self_signed' => true, 'verify_peer_name' => false, 'verify_peer' => false, 'tlsv1.2' => true)));
```

The output of the above code should be a transport object that is configured to use TLS 1.2.

## Code explanation


- `$transport`: This is the transport object that will be used to send emails.
- `Swift_SmtpTransport`: This is the class used to create the transport object.
- `smtp.example.org`: This is the SMTP server address.
- `465`: This is the port used for SMTP connections.
- `ssl`: This is the encryption type used for SMTP connections.
- `setUsername` and `setPassword`: These methods are used to set the username and password for the SMTP server.
- `setEncryption`: This method is used to set the encryption type to `tls`.
- `setStreamOptions`: This method is used to set the `tlsv1.2` option to `true`.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [PHP Manual - Swift_SmtpTransport](https://www.php.net/manual/en/class.swift-smtptransport.php)

onelinerhub: [How to use TLS 1.2 with Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-use-tls-1.2-with-swiftmailer)