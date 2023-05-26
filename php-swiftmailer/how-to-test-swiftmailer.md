# How to test Swiftmailer?
// plain

Swiftmailer is a popular library for sending emails in PHP. It can be tested using a combination of unit tests and functional tests.

Unit tests can be used to test the individual components of Swiftmailer, such as the message formatting, the transport layer, and the authentication mechanisms.

Functional tests can be used to test the entire email sending process, from the message formatting to the delivery of the email.

## Example code

```php
<?php
use Swift_Mailer;
use Swift_Message;
use Swift_SmtpTransport;

// Create the Transport
$transport = (new Swift_SmtpTransport('smtp.example.org', 25))
  ->setUsername('your username')
  ->setPassword('your password')
;

// Create the Mailer using your created Transport
$mailer = new Swift_Mailer($transport);

// Create a message
$message = (new Swift_Message('Test Subject'))
  ->setFrom(['john@doe.com' => 'John Doe'])
  ->setTo(['receiver@domain.org', 'other@domain.org' => 'A name'])
  ->setBody('Here is the message itself')
;

// Send the message
$result = $mailer->send($message);
```

## Output example

```
int(1)
```

## Code explanation


- `use Swift_Mailer;`: This imports the Swift_Mailer class, which is used to send emails.
- `use Swift_Message;`: This imports the Swift_Message class, which is used to create the message to be sent.
- `use Swift_SmtpTransport;`: This imports the Swift_SmtpTransport class, which is used to create the transport layer for sending emails.
- `$transport = (new Swift_SmtpTransport('smtp.example.org', 25))`: This creates a new Swift_SmtpTransport object, which is used to create the transport layer for sending emails.
- `->setUsername('your username')`: This sets the username for the transport layer.
- `->setPassword('your password')`: This sets the password for the transport layer.
- `$mailer = new Swift_Mailer($transport);`: This creates a new Swift_Mailer object, which is used to send emails.
- `$message = (new Swift_Message('Test Subject'))`: This creates a new Swift_Message object, which is used to create the message to be sent.
- `->setFrom(['john@doe.com' => 'John Doe'])`: This sets the sender of the message.
- `->setTo(['receiver@domain.org', 'other@domain.org' => 'A name'])`: This sets the recipients of the message.
- `->setBody('Here is the message itself')`: This sets the body of the message.
- `$result = $mailer->send($message);`: This sends the message.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [Testing Swiftmailer](https://swiftmailer.symfony.com/docs/testing.html)

onelinerhub: [How to test Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-test-swiftmailer)