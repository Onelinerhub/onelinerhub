# How to send HTML emails with Swiftmailer?
// plain

Swiftmailer is a popular library for sending HTML emails in PHP. It is easy to use and provides a lot of flexibility.

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
  ->setBody('Here is the message itself')
  ->addPart('<q>Here is the message itself</q>', 'text/html');

// Send the message
$result = $mailer->send($message);
```

## Output example

```
int(1)
```

## Code explanation


1. `require_once 'lib/swift_required.php';` - This line requires the Swift Mailer library.
2. `$transport = Swift_SmtpTransport::newInstance('smtp.example.org', 25)` - This line creates the transport using the SMTP server and port.
3. `->setUsername('yourusername')` - This line sets the username for the SMTP server.
4. `->setPassword('yourpassword')` - This line sets the password for the SMTP server.
5. `$mailer = Swift_Mailer::newInstance($transport);` - This line creates the mailer using the created transport.
6. `$message = Swift_Message::newInstance('Wonderful Subject')` - This line creates a message with the given subject.
7. `->setFrom(array('john@doe.com' => 'John Doe'))` - This line sets the sender of the message.
8. `->setTo(array('receiver@domain.org', 'other@domain.org' => 'A name'))` - This line sets the recipient of the message.
9. `->setBody('Here is the message itself')` - This line sets the plain text body of the message.
10. `->addPart('<q>Here is the message itself</q>', 'text/html')` - This line adds an HTML part to the message.
11. `$result = $mailer->send($message);` - This line sends the message.

## Helpful links

- [Swift Mailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [Swift Mailer GitHub Repository](https://github.com/swiftmailer/swiftmailer)

onelinerhub: [How to send HTML emails with Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-send-html-emails-with-swiftmailer)