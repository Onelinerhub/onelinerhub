# How to dispatch PCNTL signals in PHP?
// plain

Dispatching PCNTL signals in PHP is a way to handle signals sent to a process. It can be used to catch and handle signals sent to the script, such as `SIGTERM` or `SIGINT`.

## Example code

```php
// Setup signal handler
declare(ticks = 1);
pcntl_signal(SIGTERM, "signal_handler");

// Signal handler function
function signal_handler($signal) {
    switch($signal) {
        case SIGTERM:
            // Do something
            break;
    }
}
```

## Output example

```
None
```

## Code explanation

- `declare(ticks = 1)`: This tells PHP to check for any signals every time it executes a statement.
- `pcntl_signal(SIGTERM, "signal_handler")`: This registers the signal handler function for the `SIGTERM` signal.
- `switch($signal)`: This checks which signal was sent to the script.
- `case SIGTERM:`: This is the code that will be executed when the `SIGTERM` signal is sent.

## Helpful links
- [PHP PCNTL Manual](https://www.php.net/manual/en/ref.pcntl.php)

onelinerhub: [How to dispatch PCNTL signals in PHP?](https://onelinerhub.com/php-pcntl/how-to-dispatch-pcntl-signals-in-php)