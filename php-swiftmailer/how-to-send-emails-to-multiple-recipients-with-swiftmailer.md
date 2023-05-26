# How to send emails to multiple recipients with Swiftmailer?
// plain

Swiftmailer is a popular library for sending emails in PHP. It can be used to send emails to multiple recipients in a few simple steps.

```
<?php
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

echo $result;
```

## Output example

```
2
```

The code above will send an email to two recipients. It starts by creating a transport object with the SMTP server details. Then a mailer object is created using the transport object. Finally, a message object is created with the sender and recipient details, and the message body. The message is then sent using the mailer object, and the result is echoed.

Parts of the code:
- `$transport`: This is the transport object which contains the SMTP server details.
- `$mailer`: This is the mailer object which is used to send the message.
- `$message`: This is the message object which contains the sender and recipient details, and the message body.
- `$result`: This is the result of sending the message.

## Helpful links
- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to send emails to multiple recipients with Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-send-emails-to-multiple-recipients-with-swiftmailer)