# How to use pcntl_fork in PHP?
// plain

PCNTL stands for Process Control, and is a library of functions for PHP that allow you to create and manage processes. The `pcntl_fork()` function is used to create a new process from the current process.

```php
<?php
$pid = pcntl_fork();

if ($pid == -1) {
    die('could not fork');
} else if ($pid) {
    // parent process
    pcntl_wait($status); //Protect against Zombie children
} else {
    // child process
    echo "I'm a child process!";
    exit();
}
```

## Output example

```
I'm a child process!
```

## Code explanation

- `pcntl_fork()`: creates a new process from the current process
- `if ($pid == -1)`: checks if the process was created successfully
- `else if ($pid)`: executes the parent process
- `else`: executes the child process
- `pcntl_wait($status)`: protects against Zombie children

## Helpful links
- [PHP: pcntl_fork - Manual](https://www.php.net/manual/en/function.pcntl-fork.php)
- [PHP: pcntl_wait - Manual](https://www.php.net/manual/en/function.pcntl-wait.php)

onelinerhub: [How to use pcntl_fork in PHP?](https://onelinerhub.com/php-pcntl/how-to-use-pcntl_fork-in-php)