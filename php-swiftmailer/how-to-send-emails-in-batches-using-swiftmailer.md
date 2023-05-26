# How to send emails in batches using Swiftmailer?
// plain

Swiftmailer is a popular library for sending emails in batches. It provides an easy-to-use API for sending emails in batches.

## Example code

```
<?php
// Require the Swift Mailer library
require_once 'vendor/swiftmailer/swiftmailer/lib/swift_required.php';

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

// Print the result
echo $result;
```

## Output example

```
2
```

## Code explanation

- `require_once 'vendor/swiftmailer/swiftmailer/lib/swift_required.php';`: This line requires the Swift Mailer library.
- `$transport = Swift_SmtpTransport::newInstance('smtp.example.org', 25)`: This line creates the transport using the SMTP server.
- `->setUsername('yourusername')`: This line sets the username for the SMTP server.
- `->setPassword('yourpassword')`: This line sets the password for the SMTP server.
- `$mailer = Swift_Mailer::newInstance($transport);`: This line creates the mailer using the created transport.
- `$message = Swift_Message::newInstance('Wonderful Subject')`: This line creates a message.
- `->setFrom(array('john@doe.com' => 'John Doe'))`: This line sets the sender of the message.
- `->setTo(array('receiver@domain.org', 'other@domain.org' => 'A name'))`: This line sets the recipients of the message.
- `->setBody('Here is the message itself');`: This line sets the body of the message.
- `$result = $mailer->send($message);`: This line sends the message.
- `echo $result;`: This line prints the result of the message sending.

## Helpful links
- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to send emails in batches using Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-send-emails-in-batches-using-swiftmailer)