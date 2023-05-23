# How to send emails in Symfony with PHP?
// plain

Sending emails in Symfony with PHP is a simple process.

First, create a `Swift_Message` object with the necessary parameters:

```php
$message = (new Swift_Message('Subject'))
    ->setFrom(['john@doe.com' => 'John Doe'])
    ->setTo(['receiver@domain.org', 'other@domain.org' => 'A name'])
    ->setBody('Here is the message itself')
;
```

Then, use the `mailer` service to send the message:

```php
$mailer->send($message);
```

The `Swift_Message` object takes the following parameters:

- `Subject`: The subject of the email
- `From`: An array of sender's email address and name
- `To`: An array of receiver's email address and name
- `Body`: The body of the email

## Helpful links

- [Swift Mailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)
- [Symfony Mailer Documentation](https://symfony.com/doc/current/mailer.html)

onelinerhub: [How to send emails in Symfony with PHP?](https://onelinerhub.com/php-symfony/how-to-send-emails-in-symfony-with-php)