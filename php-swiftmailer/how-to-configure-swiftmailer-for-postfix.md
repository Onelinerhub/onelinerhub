# How to configure Swiftmailer for Postfix?
// plain

Swiftmailer is a popular library for sending emails in PHP. It can be configured to use Postfix as the mail transport agent.

To configure Swiftmailer for Postfix, you need to create a `Swift_SmtpTransport` instance and set the host, port, encryption type, and authentication credentials.

```php
$transport = (new Swift_SmtpTransport('smtp.example.com', 25))
  ->setUsername('your_username')
  ->setPassword('your_password');
```

The code above creates a `Swift_SmtpTransport` instance with the host `smtp.example.com` and port `25`. It also sets the username and password for authentication.

Once the transport is configured, you can create a `Swift_Mailer` instance and pass the transport instance to it.

```php
$mailer = new Swift_Mailer($transport);
```

You can then use the `$mailer` instance to send emails using Swiftmailer.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [Postfix Documentation](http://www.postfix.org/documentation.html)

onelinerhub: [How to configure Swiftmailer for Postfix?](https://onelinerhub.com/php-swiftmailer/how-to-configure-swiftmailer-for-postfix)