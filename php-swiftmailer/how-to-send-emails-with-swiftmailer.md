# How to send emails with Swiftmailer?
// plain

Sending emails with Swiftmailer is easy and straightforward.

```php
// Create the Transport
$transport = (new Swift_SmtpTransport('smtp.example.org', 25))
  ->setUsername('your username')
  ->setPassword('your password')
;

// Create the Mailer using your created Transport
$mailer = new Swift_Mailer($transport);

// Create a message
$message = (new Swift_Message('Wonderful Subject'))
  ->setFrom(['john@doe.com' => 'John Doe'])
  ->setTo(['receiver@domain.org', 'other@domain.org' => 'A name'])
  ->setBody('Here is the message itself')
  ;

// Send the message
$result = $mailer->send($message);
```

The output of the example code is `$result` which is an integer representing the number of successful recipients.

## Code explanation


1. `$transport`: This is the transport object which is responsible for sending the message. It requires the SMTP server address and port.
2. `$mailer`: This is the mailer object which is responsible for sending the message using the transport object.
3. `$message`: This is the message object which contains the message details such as sender, recipient, subject and body.
4. `$result`: This is the result of the send operation which is an integer representing the number of successful recipients.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [Swiftmailer GitHub Repository](https://github.com/swiftmailer/swiftmailer)

onelinerhub: [How to send emails with Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-send-emails-with-swiftmailer)