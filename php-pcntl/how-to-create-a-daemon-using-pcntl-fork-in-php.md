# How to create a daemon using PCNTL fork in PHP?
// plain

Creating a daemon using PCNTL fork in PHP is a simple process. The following example code will create a daemon that will run in the background and output a message every 5 seconds:

```
<?php

declare(ticks = 1);

pcntl_signal(SIGCHLD, SIG_IGN);

$pid = pcntl_fork();

if ($pid == -1) {
    die('could not fork');
} else if ($pid) {
    // parent process
    exit();
} else {
    // child process
    while (true) {
        echo "I'm a daemon\n";
        sleep(5);
    }
}
```

## Output example

```
I'm a daemon
I'm a daemon
I'm a daemon
...
```

The code consists of the following parts:

1. `declare(ticks = 1)`: This sets the number of ticks that PHP will wait before running signal handlers.

2. `pcntl_signal(SIGCHLD, SIG_IGN)`: This tells PHP to ignore the SIGCHLD signal, which is sent when a child process terminates.

3. `pcntl_fork()`: This creates a child process.

4. `if ($pid == -1)`: This checks if the fork failed.

5. `else if ($pid)`: This is the parent process.

6. `else`: This is the child process.

7. `while (true)`: This creates an infinite loop.

8. `echo "I'm a daemon\n"`: This outputs a message.

9. `sleep(5)`: This pauses the loop for 5 seconds.

## Helpful links

- [PHP: pcntl_fork - Manual](https://www.php.net/manual/en/function.pcntl-fork.php)
- [PHP: pcntl_signal - Manual](https://www.php.net/manual/en/function.pcntl-signal.php)

onelinerhub: [How to create a daemon using PCNTL fork in PHP?](https://onelinerhub.com/php-pcntl/how-to-create-a-daemon-using-pcntl-fork-in-php)