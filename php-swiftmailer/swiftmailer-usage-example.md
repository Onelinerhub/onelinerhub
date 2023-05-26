# Swiftmailer usage example
// plain

Swiftmailer is a popular library for sending emails in PHP. It is easy to use and provides a lot of features.

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

- `require_once 'lib/swift_required.php'` - this line includes the Swift Mailer library
- `$transport = Swift_SmtpTransport::newInstance('smtp.example.org', 25)` - this line creates a new SMTP transport instance
- `->setUsername('yourusername')` - this line sets the username for the SMTP server
- `->setPassword('yourpassword')` - this line sets the password for the SMTP server
- `$mailer = Swift_Mailer::newInstance($transport)` - this line creates a new mailer instance using the created transport
- `$message = Swift_Message::newInstance('Wonderful Subject')` - this line creates a new message instance
- `->setFrom(array('john@doe.com' => 'John Doe'))` - this line sets the sender of the message
- `->setTo(array('receiver@domain.org', 'other@domain.org' => 'A name'))` - this line sets the recipients of the message
- `->setBody('Here is the message itself')` - this line sets the body of the message
- `$result = $mailer->send($message)` - this line sends the message

## Helpful links
- [Swift Mailer official website](https://swiftmailer.symfony.com/)
- [Swift Mailer documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [Swiftmailer usage example](https://onelinerhub.com/php-swiftmailer/swiftmailer-usage-example)