# How to set the 'from' address in Swiftmailer?
// plain

The 'from' address in Swiftmailer can be set using the `setFrom()` method.

```
$message->setFrom('sender@example.com', 'Sender Name');
```

The `setFrom()` method takes two parameters:

1. The email address of the sender.
2. The name of the sender.

The `setFrom()` method should be called before the `send()` method.

For more information, please refer to the [Swiftmailer documentation](https://swiftmailer.symfony.com/docs/sending.html#setting-the-from-address).

onelinerhub: [How to set the 'from' address in Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-set-the--from--address-in-swiftmailer)