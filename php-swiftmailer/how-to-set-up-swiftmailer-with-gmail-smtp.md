# How to set up Swiftmailer with Gmail SMTP?
// plain

Swiftmailer is a popular library for sending emails from PHP applications. Setting up Swiftmailer with Gmail SMTP is easy and straightforward.

```php
// Create the Transport
$transport = (new Swift_SmtpTransport('smtp.gmail.com', 465, 'ssl'))
  ->setUsername('yourusername@gmail.com')
  ->setPassword('yourpassword');

// Create the Mailer using your created Transport
$mailer = new Swift_Mailer($transport);

// Create a message
$message = (new Swift_Message('Wonderful Subject'))
  ->setFrom(['john@doe.com' => 'John Doe'])
  ->setTo(['receiver@domain.org', 'other@domain.org' => 'A name'])
  ->setBody('Here is the message itself');

// Send the message
$result = $mailer->send($message);
```

The output of the example code is `$result` which is an integer representing the number of successful recipients.

## Code explanation


1. `$transport`: This is the transport object which is used to connect to the Gmail SMTP server. It requires the hostname, port and encryption type as parameters.

2. `$mailer`: This is the mailer object which is used to send the message. It requires the transport object as a parameter.

3. `$message`: This is the message object which is used to create the email. It requires the from, to, subject and body as parameters.

4. `$result`: This is the result of the send operation which is an integer representing the number of successful recipients.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [Gmail SMTP Settings](https://support.google.com/a/answer/176600?hl=en)

onelinerhub: [How to set up Swiftmailer with Gmail SMTP?](https://onelinerhub.com/php-swiftmailer/how-to-set-up-swiftmailer-with-gmail-smtp)