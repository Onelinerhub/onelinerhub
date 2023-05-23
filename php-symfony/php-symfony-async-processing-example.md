# PHP Symfony async processing example
// plain

An example of asynchronous processing in PHP Symfony is using the [Symfony Messenger Component](https://symfony.com/doc/current/components/messenger.html). This component allows you to send messages to a message bus, which can then be processed asynchronously.

```php
// Create a message
$message = new MyMessage('Hello world!');

// Send the message to the message bus
$bus->dispatch($message);
```

The message bus will then process the message asynchronously. The output of this example code will be `null`.

## Code explanation


1. Create a message: This creates a new message object, which contains the data to be processed.
2. Send the message to the message bus: This sends the message to the message bus, which will then process it asynchronously.
3. Output: The output of this example code will be `null`.

## Helpful links

- [Symfony Messenger Component](https://symfony.com/doc/current/components/messenger.html)

onelinerhub: [PHP Symfony async processing example](https://onelinerhub.com/php-symfony/php-symfony-async-processing-example)