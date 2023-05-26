# How to send emails in UTF8 using Swiftmailer?
// plain

Swiftmailer supports sending emails in UTF8. To do this, you need to set the charset of the message to UTF8. This can be done by using the `setCharset()` method of the `Swift_Message` class.

```php
$message = new Swift_Message();
$message->setCharset('UTF-8');
```

The code above will set the charset of the message to UTF8.

## Code explanation


- `$message`: This is an instance of the `Swift_Message` class.
- `setCharset()`: This is a method of the `Swift_Message` class which sets the charset of the message.
- `'UTF-8'`: This is the charset which is being set for the message.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to send emails in UTF8 using Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-send-emails-in-utf8-using-swiftmailer)