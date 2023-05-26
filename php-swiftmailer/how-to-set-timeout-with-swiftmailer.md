# How to set timeout with Swiftmailer?
// plain

Swiftmailer provides a way to set a timeout for sending emails. This can be done by setting the `timeout` parameter in the `Transport` configuration.

```php
$transport = (new Swift_SmtpTransport('smtp.example.org', 25))
  ->setTimeout(30);
```

The above example sets the timeout to 30 seconds.

## Code explanation


- `Swift_SmtpTransport`: This is the transport class used to send emails.
- `smtp.example.org`: This is the SMTP server address.
- `25`: This is the port used to connect to the SMTP server.
- `setTimeout`: This is the method used to set the timeout.
- `30`: This is the timeout value in seconds.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to set timeout with Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-set-timeout-with-swiftmailer)