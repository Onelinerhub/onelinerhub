# How to use pcntl_wait in PHP?
// plain

PCNTL_WAIT is a PHP function used to wait for a child process to finish executing. It is part of the Process Control (PCNTL) extension.

## Example

```
<?php
$pid = pcntl_fork();
if ($pid == -1) {
    die('could not fork');
} else if ($pid) {
    // parent process
    pcntl_wait($status); //Protect against Zombie children
} else {
    // child process
    // do some work
    exit();
}
?>
```

The code above will create a child process and wait for it to finish executing before continuing.

## Code explanation

- pcntl_fork(): Creates a child process
- pcntl_wait($status): Waits for the child process to finish executing
- exit(): Exits the child process

## Helpful links
- [PHP PCNTL_WAIT Manual](https://www.php.net/manual/en/function.pcntl-wait.php)
- [PHP PCNTL Manual](https://www.php.net/manual/en/book.pcntl.php)

onelinerhub: [How to use pcntl_wait in PHP?](https://onelinerhub.com/php-pcntl/how-to-use-pcntl_wait-in-php)