# How to set the default 'from' address in Swiftmailer?
// plain

Swiftmailer allows you to set the default 'from' address for all emails sent using the library. This can be done by setting the `from` property of the `message` object.

```php
$message->setFrom('sender@example.com');
```

The `setFrom()` method takes two parameters:

1. `$address` - The email address of the sender.
2. `$name` - The name of the sender (optional).

For more information, please refer to the [Swiftmailer documentation](https://swiftmailer.symfony.com/docs/sending.html#setting-the-from-address).

onelinerhub: [How to set the default 'from' address in Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-set-the-default--from--address-in-swiftmailer)