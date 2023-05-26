# How to set the sender name in SwiftMailer?
// plain

SwiftMailer allows you to set the sender name in the message header. To do this, you need to use the `setFrom()` method.

```php
$message->setFrom(['john@doe.com' => 'John Doe']);
```

This will set the sender name to "John Doe" and the sender address to "john@doe.com".

The `setFrom()` method takes two parameters:

1. The sender address - This is the email address of the sender.
2. The sender name - This is the name of the sender that will be displayed in the message header.

## Helpful links

- [SwiftMailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to set the sender name in SwiftMailer?](https://onelinerhub.com/php-swiftmailer/how-to-set-the-sender-name-in-swiftmailer)