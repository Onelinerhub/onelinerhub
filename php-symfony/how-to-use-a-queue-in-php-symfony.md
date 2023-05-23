# How to use a queue in PHP Symfony?
// plain

A queue is a data structure that allows you to store and process data in a specific order. In PHP Symfony, queues can be used to manage tasks such as sending emails, processing images, and more.

## Example code

```
use Symfony\Component\Messenger\MessageBusInterface;

class MyService
{
    private $bus;

    public function __construct(MessageBusInterface $bus)
    {
        $this->bus = $bus;
    }

    public function doSomething()
    {
        $this->bus->dispatch(new MyMessage());
    }
}
```

## Output example

```
No output
```

## Code explanation

- `use Symfony\Component\Messenger\MessageBusInterface;`: This imports the MessageBusInterface class from the Symfony Messenger component.
- `private $bus;`: This declares a private property to store the MessageBusInterface instance.
- `public function __construct(MessageBusInterface $bus)`: This is the constructor for the class. It takes a MessageBusInterface instance as an argument and stores it in the `$bus` property.
- `public function doSomething()`: This is a method that dispatches a message to the queue.
- `$this->bus->dispatch(new MyMessage());`: This dispatches a new message to the queue.

## Helpful links
- [Symfony Messenger Component](https://symfony.com/doc/current/components/messenger.html)

onelinerhub: [How to use a queue in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-a-queue-in-php-symfony)