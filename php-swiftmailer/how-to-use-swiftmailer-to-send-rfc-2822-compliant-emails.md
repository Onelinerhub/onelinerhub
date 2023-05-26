# How to use Swiftmailer to send RFC 2822 compliant emails?
// plain

Swiftmailer is a popular library for sending emails in PHP. It can be used to send RFC 2822 compliant emails.

## Example code

```
<?php
// Require the Swift Mailer library
require_once 'lib/swift_required.php';

// Create the Transport
$transport = Swift_SmtpTransport::newInstance('smtp.example.org', 25)
  ->setUsername('yourusername')
  ->setPassword('yourpassword');

// Create the Mailer using your created Transport
$mailer = Swift_Mailer::newInstance($transport);

// Create a message
$message = Swift_Message::newInstance('Wonderful Subject')
  ->setFrom(array('john@doe.com' => 'John Doe'))
  ->setTo(array('receiver@domain.org', 'other@domain.org' => 'A name'))
  ->setBody('Here is the message itself');

// Send the message
$result = $mailer->send($message);
```

## Output example

```
int(1)
```

## Code explanation

- `require_once 'lib/swift_required.php'`: This line requires the Swift Mailer library.
- `$transport = Swift_SmtpTransport::newInstance('smtp.example.org', 25)`: This line creates a new SMTP transport instance.
- `->setUsername('yourusername')` and `->setPassword('yourpassword')`: These lines set the username and password for the SMTP server.
- `$mailer = Swift_Mailer::newInstance($transport)`: This line creates a new mailer instance using the transport instance.
- `$message = Swift_Message::newInstance('Wonderful Subject')`: This line creates a new message instance.
- `->setFrom(array('john@doe.com' => 'John Doe'))` and `->setTo(array('receiver@domain.org', 'other@domain.org' => 'A name'))`: These lines set the sender and recipient of the message.
- `->setBody('Here is the message itself')`: This line sets the body of the message.
- `$result = $mailer->send($message)`: This line sends the message.

## Helpful links
- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [RFC 2822](https://tools.ietf.org/html/rfc2822)

onelinerhub: [How to use Swiftmailer to send RFC 2822 compliant emails?](https://onelinerhub.com/php-swiftmailer/how-to-use-swiftmailer-to-send-rfc-2822-compliant-emails)