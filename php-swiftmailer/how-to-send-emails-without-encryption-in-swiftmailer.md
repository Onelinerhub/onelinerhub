# How to send emails without encryption in SwiftMailer?
// plain

SwiftMailer can be used to send emails without encryption. To do this, you need to create a `Swift_Message` object and set the `setEncryption` method to `null`.

```php
$message = new Swift_Message();
$message->setEncryption(null);
```

The code above will create a `Swift_Message` object and set the encryption to `null`.

To send the email, you need to create a `Swift_Mailer` object and call the `send()` method with the `Swift_Message` object as an argument.

```php
$mailer = new Swift_Mailer();
$mailer->send($message);
```

The code above will create a `Swift_Mailer` object and send the email with the `Swift_Message` object.

## Code explanation


- `Swift_Message`: This is an object used to create an email message.
- `setEncryption()`: This is a method used to set the encryption for the email message.
- `Swift_Mailer`: This is an object used to send the email message.
- `send()`: This is a method used to send the email message.

## Helpful links

- [SwiftMailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to send emails without encryption in SwiftMailer?](https://onelinerhub.com/php-swiftmailer/how-to-send-emails-without-encryption-in-swiftmailer)