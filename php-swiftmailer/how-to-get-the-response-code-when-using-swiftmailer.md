# How to get the response code when using Swiftmailer?
// plain

Swiftmailer provides a way to get the response code when sending an email. The `getResponse()` method of the `Swift_Transport_AbstractSmtpTransport` class can be used to get the response code.

## Example code

```
$transport = Swift_SmtpTransport::newInstance('smtp.example.org', 25);
$mailer = Swift_Mailer::newInstance($transport);
$message = Swift_Message::newInstance('Test Subject');
$mailer->send($message);
$responseCode = $transport->getResponse();
```

## Output example

```
250 OK
```

## Code explanation

- `Swift_SmtpTransport::newInstance('smtp.example.org', 25)`: creates a new instance of the `Swift_SmtpTransport` class, passing in the SMTP server address and port number.
- `Swift_Mailer::newInstance($transport)`: creates a new instance of the `Swift_Mailer` class, passing in the `$transport` object.
- `Swift_Message::newInstance('Test Subject')`: creates a new instance of the `Swift_Message` class, passing in the subject of the email.
- `$mailer->send($message)`: sends the email using the `$mailer` object, passing in the `$message` object.
- `$transport->getResponse()`: gets the response code from the `$transport` object.

## Helpful links
- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to get the response code when using Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-get-the-response-code-when-using-swiftmailer)