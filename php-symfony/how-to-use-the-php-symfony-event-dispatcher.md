# How to use the PHP Symfony event dispatcher?
// plain

The Symfony Event Dispatcher is a powerful tool for creating and managing events in a PHP application. It allows you to create custom events and listeners that can be triggered and handled in a variety of ways.

## Example code

```
use Symfony\Component\EventDispatcher\EventDispatcher;

$dispatcher = new EventDispatcher();

$dispatcher->addListener('my_event', function ($event) {
    // Do something with the event
});

$dispatcher->dispatch('my_event');
```

The code above creates a new EventDispatcher instance, adds a listener for the 'my_event' event, and then dispatches the event.

## Code explanation

- `use Symfony\Component\EventDispatcher\EventDispatcher;`: This imports the EventDispatcher class from the Symfony library.
- `$dispatcher = new EventDispatcher();`: This creates a new instance of the EventDispatcher class.
- `$dispatcher->addListener('my_event', function ($event) {`: This adds a listener for the 'my_event' event. The listener is a function that will be called when the event is dispatched.
- `$dispatcher->dispatch('my_event');`: This dispatches the 'my_event' event, triggering any listeners that have been added.

## Helpful links
- [Symfony Event Dispatcher Documentation](https://symfony.com/doc/current/components/event_dispatcher.html)

onelinerhub: [How to use the PHP Symfony event dispatcher?](https://onelinerhub.com/php-symfony/how-to-use-the-php-symfony-event-dispatcher)