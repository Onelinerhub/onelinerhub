# How to use the messenger component in PHP Symfony?
// plain

The Messenger component in PHP Symfony is a powerful tool for sending and receiving messages between applications. It allows you to send messages asynchronously, which can be useful for tasks such as sending emails or performing background tasks.

## Example code

```php
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
- `public function __construct(MessageBusInterface $bus)`: This is the constructor for the class, which takes a MessageBusInterface instance as an argument.
- `$this->bus = $bus;`: This assigns the MessageBusInterface instance to the private property.
- `$this->bus->dispatch(new MyMessage());`: This dispatches a message using the MessageBusInterface instance.

## Helpful links
- [Symfony Messenger Documentation](https://symfony.com/doc/current/components/messenger.html)

onelinerhub: [How to use the messenger component in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-the-messenger-component-in-php-symfony)