# How to test SMTP connection with Swiftmailer?
// plain

Testing SMTP connection with Swiftmailer is easy and straightforward.

```php
<?php
// Create the Transport
$transport = (new Swift_SmtpTransport('smtp.example.org', 25))
  ->setUsername('your username')
  ->setPassword('your password')
;

// Create the Mailer using your created Transport
$mailer = new Swift_Mailer($transport);

// Send a message
$message = (new Swift_Message('Test SMTP connection'))
  ->setFrom(['john@doe.com' => 'John Doe'])
  ->setTo(['receiver@domain.org', 'other@domain.org' => 'A name'])
  ->setBody('Here is the message itself')
  ;

$result = $mailer->send($message);

if ($result) {
    echo "Message sent successfully.";
}
```

## Output example

```
Message sent successfully.
```

1. Create the Transport: Create a new Swift_SmtpTransport object with the SMTP server address and port. Set the username and password for authentication.
2. Create the Mailer: Create a new Swift_Mailer object with the created transport.
3. Send a message: Create a new Swift_Message object with the subject and body of the message. Set the sender and receiver of the message.
4. Send the message: Use the send() method of the mailer object to send the message.
5. Check the result: Check the result of the send() method to see if the message was sent successfully.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to test SMTP connection with Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-test-smtp-connection-with-swiftmailer)