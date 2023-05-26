# How to use Swiftmailer transport?
// plain

Swiftmailer transport is a library used to send emails from PHP applications. It is easy to use and provides a wide range of features.

To use Swiftmailer transport, you need to create a `Swift_Transport` instance and pass it to the `Swift_Mailer` constructor.

```php
// Create the Transport
$transport = (new Swift_SmtpTransport('smtp.example.org', 25))
  ->setUsername('your username')
  ->setPassword('your password')
;

// Create the Mailer using your created Transport
$mailer = new Swift_Mailer($transport);
```

The code above creates a `Swift_SmtpTransport` instance and passes it to the `Swift_Mailer` constructor. The `Swift_SmtpTransport` class is used to send emails via SMTP.

To send an email, you need to create a `Swift_Message` instance and pass it to the `send()` method of the `Swift_Mailer` instance.

```php
// Create a message
$message = (new Swift_Message('Wonderful Subject'))
  ->setFrom(['john@doe.com' => 'John Doe'])
  ->setTo(['receiver@domain.org', 'other@domain.org' => 'A name'])
  ->setBody('Here is the message itself')
  ;

// Send the message
$result = $mailer->send($message);
```

The code above creates a `Swift_Message` instance and passes it to the `send()` method of the `Swift_Mailer` instance. The `send()` method returns the number of successful recipients.

## Helpful links
- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [Swiftmailer Transport](https://swiftmailer.symfony.com/docs/transport.html)

onelinerhub: [How to use Swiftmailer transport?](https://onelinerhub.com/php-swiftmailer/how-to-use-swiftmailer-transport)