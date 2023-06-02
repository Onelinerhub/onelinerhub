# How do I set the retry interval for a PHP application using Redis?
// plain

The retry interval for a PHP application using Redis can be set using the `RetryStrategy` class.

```
<?php
use Predis\RetryStrategy;

$client = new Predis\Client([
    'retry_strategy' => new RetryStrategy\ExponentialBackoff(2, 100)
]);
```

The code above sets the retry interval to an exponential backoff of 2 retries with an interval of 100 milliseconds.

The code consists of the following parts:

1. `use Predis\RetryStrategy;` - This imports the RetryStrategy class from the Predis library.
2. `$client = new Predis\Client([])` - This creates a new client object.
3. `'retry_strategy' => new RetryStrategy\ExponentialBackoff(2, 100)` - This sets the retry strategy to an exponential backoff of 2 retries with an interval of 100 milliseconds.

For more information, see the [Predis documentation](https://github.com/nrk/predis/blob/develop/doc/connecting.md#connection-options).

onelinerhub: [How do I set the retry interval for a PHP application using Redis?](https://onelinerhub.com/predis/how-do-i-set-the-retry-interval-for-a-php-application-using-redis)