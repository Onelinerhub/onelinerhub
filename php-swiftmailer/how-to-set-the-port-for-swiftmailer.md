# How to set the port for Swiftmailer?
// plain

Swiftmailer can be configured to use a specific port for sending emails.

```php
// Create the Transport
$transport = (new Swift_SmtpTransport('smtp.example.org', 25))
  ->setUsername('your username')
  ->setPassword('your password')
;

// Create the Mailer using your created Transport
$mailer = new Swift_Mailer($transport);
```

The example code above creates a transport object with the hostname `smtp.example.org` and port `25`.

## Code explanation


- `Swift_SmtpTransport`: This is the class used to create a transport object.
- `smtp.example.org`: This is the hostname of the SMTP server.
- `25`: This is the port number used to connect to the SMTP server.
- `setUsername` and `setPassword`: These methods are used to set the username and password for authentication.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to set the port for Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-set-the-port-for-swiftmailer)