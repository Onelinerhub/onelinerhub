# listener

How do I implement an event listener using PHP Omnipay?
// plain

A listener in PHP Omnipay is an event handler that is triggered when an event occurs. To implement an event listener, you need to create a class that implements the `Omnipay\Common\Event\AbstractEventListener` interface. The class must include three methods: `getEvents`, `handleEvent`, and `getName`.

The `getEvents` method is used to define which events the listener should listen for. It should return an array of event names. For example:

```
public function getEvents()
{
    return array('payment.success', 'payment.failure');
}
```

The `handleEvent` method is called when an event is triggered. It should accept two parameters - the event name and an array of parameters. For example:

```
public function handleEvent($eventName, array $parameters)
{
    // Handle the event here
}
```

The `getName` method is used to return the name of the listener. It should return a string. For example:

```
public function getName()
{
    return 'MyListener';
}
```

Once the class has been created, it can be registered with the `Omnipay\Common\Event\EventDispatcher` class. For example:

```
$dispatcher = new \Omnipay\Common\Event\EventDispatcher();
$dispatcher->addListener(new MyListener());
```

When an event is triggered, the `handleEvent` method of the listener will be called.

## Helpful links

- [PHP Omnipay Documentation](https://github.com/thephpleague/omnipay)
- [Event Dispatcher Documentation](https://github.com/thephpleague/omnipay-common/blob/master/src/Event/EventDispatcher.php)

onelinerhub: [listener

How do I implement an event listener using PHP Omnipay?](https://onelinerhub.com/php-omnipay/listener--how-do-i-implement-an-event-listener-using-php-omnipay)