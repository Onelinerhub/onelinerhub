# How to kill a process with PHP PCNTL?
// plain

Using the PHP PCNTL extension, you can kill a process with the `pcntl_kill()` function.

```php
<?php
$pid = 1234;
pcntl_kill($pid, SIGKILL);
```

The `pcntl_kill()` function takes two parameters:

1. `$pid` - The process ID of the process to be killed.
2. `SIGKILL` - The signal to be sent to the process. In this case, `SIGKILL` is used to force the process to terminate.

For more information, see the [PHP PCNTL documentation](https://www.php.net/manual/en/ref.pcntl.php).

onelinerhub: [How to kill a process with PHP PCNTL?](https://onelinerhub.com/php-pcntl/how-to-kill-a-process-with-php-pcntl)