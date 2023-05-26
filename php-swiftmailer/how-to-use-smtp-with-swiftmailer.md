# How to use SMTP with Swiftmailer?
// plain

Swiftmailer is a popular library for sending emails using PHP. It supports sending emails using SMTP protocol. To use SMTP with Swiftmailer, you need to create a `Swift_SmtpTransport` instance and pass it to `Swift_Mailer` instance.

```php
// Create the Transport
$transport = (new Swift_SmtpTransport('smtp.example.org', 25))
  ->setUsername('your username')
  ->setPassword('your password')
;

// Create the Mailer using your created Transport
$mailer = new Swift_Mailer($transport);
```

The code above creates a `Swift_SmtpTransport` instance with host `smtp.example.org` and port `25`, and sets the username and password for authentication. Then it creates a `Swift_Mailer` instance with the created transport.

Parts of the code:

- `Swift_SmtpTransport`: Class for sending emails using SMTP protocol.
- `smtp.example.org`: Hostname of the SMTP server.
- `25`: Port of the SMTP server.
- `setUsername()`: Method to set the username for authentication.
- `setPassword()`: Method to set the password for authentication.
- `Swift_Mailer`: Class for sending emails.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [Swift_SmtpTransport Documentation](https://swiftmailer.symfony.com/docs/sending.html#using-smtp)

onelinerhub: [How to use SMTP with Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-use-smtp-with-swiftmailer)