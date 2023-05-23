# How to use pcntl_signal in PHP?
// plain

PCNTL stands for Process Control, and is a PHP extension that allows you to execute Unix-like signals in your PHP scripts.

Using PCNTL_Signal allows you to catch signals sent to your script and handle them accordingly.

## Example

```
<?php

// Declare the signal handler
function sig_handler($signo)
{
    switch ($signo) {
        case SIGTERM:
            // handle shutdown tasks
            exit;
            break;
        case SIGHUP:
            // handle restart tasks
            break;
        case SIGUSR1:
            echo "Caught SIGUSR1\n";
            break;
        default:
            // handle all other signals
    }
}

// Setup signal handlers
pcntl_signal(SIGTERM, "sig_handler");
pcntl_signal(SIGHUP,  "sig_handler");
pcntl_signal(SIGUSR1, "sig_handler");

// Do some work
while (true) {
    sleep(1);
    echo "Working...\n";
}

?>
```
## Output example

```
Working...
Working...
Caught SIGUSR1
Working...
```

## Code explanation


1. Declare the signal handler: This is a function that will be called when a signal is received. It takes one argument, the signal number, and should contain a switch statement to handle different signals.

2. Setup signal handlers: This is where you specify which signals you want to handle and which function should be called when they are received.

3. Do some work: This is the main body of your script. It should contain the code that you want to execute.

## Helpful links

- [PHP Manual: pcntl_signal](https://www.php.net/manual/en/function.pcntl-signal.php)
- [PHP Manual: pcntl_signal_dispatch](https://www.php.net/manual/en/function.pcntl-signal-dispatch.php)
- [PHP Manual: pcntl_signal_get_handler](https://www.php.net/manual/en/function.pcntl-signal-get-handler.php)

onelinerhub: [How to use pcntl_signal in PHP?](https://onelinerhub.com/php-pcntl/how-to-use-pcntl_signal-in-php)