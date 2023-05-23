# How to use pcntl_wexitstatus in PHP?
// plain

PCNTL_WEXITSTATUS is a PHP function used to retrieve the exit status of a child process. It is part of the [pcntl](https://www.php.net/manual/en/ref.pcntl.php) extension.

## Example

```
<?php
$pid = pcntl_fork();
if ($pid == -1) {
    die('could not fork');
} else if ($pid) {
    // parent
    $status = null;
    pcntl_waitpid($pid, $status);
    $exitStatus = pcntl_wexitstatus($status);
    echo "Child exited with status $exitStatus\n";
} else {
    // child
    exit(3);
}
```

## Output example

```
Child exited with status 3
```

## Code explanation

- `pcntl_fork()`: creates a child process
- `pcntl_waitpid($pid, $status)`: waits for the child process to finish
- `pcntl_wexitstatus($status)`: retrieves the exit status of the child process

## Helpful links
- [pcntl_fork](https://www.php.net/manual/en/function.pcntl-fork.php)
- [pcntl_waitpid](https://www.php.net/manual/en/function.pcntl-waitpid.php)
- [pcntl_wexitstatus](https://www.php.net/manual/en/function.pcntl-wexitstatus.php)

onelinerhub: [How to use pcntl_wexitstatus in PHP?](https://onelinerhub.com/php-pcntl/how-to-use-pcntl_wexitstatus-in-php)