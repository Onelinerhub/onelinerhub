# How to log emails sent with Swiftmailer?
// plain

Swiftmailer is a popular library for sending emails in PHP. To log emails sent with Swiftmailer, you can use the `Swift_Plugins_LoggerPlugin` class. This class implements the `Swift_Events_EventListener` interface and allows you to log all emails sent with Swiftmailer.

## Example code

```php
<?php

// Create the Transport
$transport = (new Swift_SmtpTransport('smtp.example.org', 25))
  ->setUsername('your username')
  ->setPassword('your password')
;

// Create the Mailer using your created Transport
$mailer = new Swift_Mailer($transport);

// Create a logger
$logger = new Swift_Plugins_LoggerPlugin(
    new Swift_Plugins_Loggers_ArrayLogger()
);

// Register the logger
$mailer->registerPlugin($logger);

// Create a message
$message = (new Swift_Message('Wonderful Subject'))
  ->setFrom(['john@doe.com' => 'John Doe'])
  ->setTo(['receiver@domain.org', 'other@domain.org' => 'A name'])
  ->setBody('Here is the message itself')
;

// Send the message
$result = $mailer->send($message);

// Dump the log contents
echo $logger->dump();
```

## Output example

```
== START LOGGING ==
Sending message to: receiver@domain.org
Sending message to: other@domain.org

Sent 1 messages

== END LOGGING ==
```

## Code explanation


1. Create the Transport: This creates the transport layer for sending emails.
2. Create the Mailer: This creates the mailer object using the transport layer.
3. Create a logger: This creates a logger object for logging emails sent with Swiftmailer.
4. Register the logger: This registers the logger with the mailer object.
5. Create a message: This creates a message object with the necessary details.
6. Send the message: This sends the message using the mailer object.
7. Dump the log contents: This dumps the log contents to the screen.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [Swift_Plugins_LoggerPlugin Class](https://swiftmailer.symfony.com/api/master/class-Swift_Plugins_LoggerPlugin.html)

onelinerhub: [How to log emails sent with Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-log-emails-sent-with-swiftmailer)