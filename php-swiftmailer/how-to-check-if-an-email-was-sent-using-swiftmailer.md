# How to check if an email was sent using Swiftmailer?
// plain

Swiftmailer provides a way to check if an email was sent using its `send()` method. The `send()` method returns a `Swift_Message` object which contains a `getId()` method that can be used to check if the email was sent.

## Example code

```
$message = Swift_Message::newInstance()
    ->setSubject('Test Email')
    ->setFrom('sender@example.com')
    ->setTo('recipient@example.com')
    ->setBody('This is a test email.');

$sent = $mailer->send($message);

if ($sent) {
    echo $message->getId();
}
```

## Output example

```
<20160505095004.1.A3F8B2C7F8A@example.com>
```

## Code explanation

- `Swift_Message::newInstance()`: creates a new instance of the `Swift_Message` class.
- `setSubject()`: sets the subject of the email.
- `setFrom()`: sets the sender of the email.
- `setTo()`: sets the recipient of the email.
- `setBody()`: sets the body of the email.
- `send()`: sends the email and returns a `Swift_Message` object.
- `getId()`: returns the unique ID of the sent email.

## Helpful links
- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to check if an email was sent using Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-check-if-an-email-was-sent-using-swiftmailer)