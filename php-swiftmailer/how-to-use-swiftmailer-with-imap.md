# How to use Swiftmailer with IMAP?
// plain

Swiftmailer can be used with IMAP to send and receive emails. To use Swiftmailer with IMAP, you need to create a Transport instance with the IMAP host, port, username, and password.

```php
$transport = (new Swift_SmtpTransport('imap.example.com', 993, 'ssl'))
  ->setUsername('your@example.com')
  ->setPassword('yourpassword');
```

The code above creates a Transport instance with the IMAP host, port, username, and password.

Once the Transport instance is created, you can use it to send and receive emails.

```php
$mailer = new Swift_Mailer($transport);

$message = (new Swift_Message('Wonderful Subject'))
  ->setFrom(['john@doe.com' => 'John Doe'])
  ->setTo(['receiver@domain.org', 'other@domain.org' => 'A name'])
  ->setBody('Here is the message itself')
  ;

$result = $mailer->send($message);
```

The code above creates a Mailer instance with the Transport instance and sends an email.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [Swiftmailer IMAP Transport](https://swiftmailer.symfony.com/docs/sending.html#using-an-imap-transport)

onelinerhub: [How to use Swiftmailer with IMAP?](https://onelinerhub.com/php-swiftmailer/how-to-use-swiftmailer-with-imap)