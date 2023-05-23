# How to use PCNTL signals in PHP?
// plain

PCNTL signals are a way to handle events in PHP. They can be used to catch signals sent to the script from the operating system.

## Example code

```
<?php

declare(ticks = 1);

// Signal handler function
function signal_handler($signal) {
    switch($signal) {
        case SIGTERM:
            // handle shutdown tasks
            exit;
        case SIGKILL:
            // handle shutdown tasks
            exit;
        default:
            // handle all other signals
    }
}

// Setup signal handlers
pcntl_signal(SIGTERM, "signal_handler");
pcntl_signal(SIGKILL, "signal_handler");

// Rest of your code

?>
```

The code above sets up signal handlers for the SIGTERM and SIGKILL signals. The `pcntl_signal()` function takes two parameters, the signal to be handled and the name of the signal handler function. The `declare(ticks = 1)` statement tells PHP to check for signals after every statement.

## Code explanation

- `declare(ticks = 1)`: tells PHP to check for signals after every statement
- `pcntl_signal()`: takes two parameters, the signal to be handled and the name of the signal handler function
- `signal_handler()`: the signal handler function which handles the signals

## Helpful links
- [PHP PCNTL Manual](https://www.php.net/manual/en/ref.pcntl.php)
- [PHP PCNTL Signal Handling](https://www.php.net/manual/en/function.pcntl-signal.php)

onelinerhub: [How to use PCNTL signals in PHP?](https://onelinerhub.com/php-pcntl/how-to-use-pcntl-signals-in-php)