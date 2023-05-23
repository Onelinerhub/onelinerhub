# How to use pcntl_waitpid in PHP?
// plain

PCNTL_WAITPID is a PHP function used to wait for a child process to terminate. It takes two parameters, the first being the PID of the process to wait for, and the second being a variable to store the status of the child process.

```
<?php
$pid = pcntl_fork();
if ($pid == -1) {
    die('could not fork');
} else if ($pid) {
    // parent
    $status = null;
    pcntl_waitpid($pid, $status);
} else {
    // child
    exit();
}
```

The output of the above code will be nothing, as the child process exits immediately.

## Code explanation


1. `pcntl_fork()` - This function creates a child process.
2. `pcntl_waitpid($pid, $status)` - This function waits for the child process to terminate, and stores the status of the child process in the second parameter.
3. `exit()` - This function exits the child process.

## Helpful links

- [PHP pcntl_waitpid Manual](https://www.php.net/manual/en/function.pcntl-waitpid.php)
- [PHP pcntl_fork Manual](https://www.php.net/manual/en/function.pcntl-fork.php)

onelinerhub: [How to use pcntl_waitpid in PHP?](https://onelinerhub.com/php-pcntl/how-to-use-pcntl_waitpid-in-php)