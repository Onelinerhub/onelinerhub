# How to process async tasks in PHP Symfony?
// plain

Processing async tasks in PHP Symfony can be done using the [Symfony Messenger Component](https://symfony.com/doc/current/components/messenger.html). It provides a message bus system that allows you to send and receive messages asynchronously.

## Example code

```php
// Create a message
$message = new MyMessage('Hello world!');

// Send the message
$bus->dispatch($message);
```

The code above creates a message object and dispatches it to the message bus. The message bus will then handle the message asynchronously.

## Code explanation


1. Create a message object: `$message = new MyMessage('Hello world!');`
2. Dispatch the message to the message bus: `$bus->dispatch($message);`

## Helpful links

- [Symfony Messenger Component](https://symfony.com/doc/current/components/messenger.html)

onelinerhub: [How to process async tasks in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-process-async-tasks-in-php-symfony)