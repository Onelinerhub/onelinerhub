# How to use the PCNTL_FORK function in PHP?
// plain

The PCNTL_FORK function in PHP is used to create a child process from the parent process. It is used to execute multiple tasks simultaneously.

## Example code

```
<?php
$pid = pcntl_fork();

if ($pid == -1) {
     die('could not fork');
} else if ($pid) {
     // we are the parent
     pcntl_wait($status); //Protect against Zombie children
} else {
     // we are the child
     echo "I'm the child\n";
}
?>
```

## Output example

```
I'm the child
```

## Code explanation


1. `$pid = pcntl_fork();` - This line creates a child process from the parent process and stores the process id of the child process in the `$pid` variable.

2. `if ($pid == -1) {` - This line checks if the child process was created successfully. If the value of `$pid` is `-1`, it means that the child process was not created successfully.

3. `else if ($pid) {` - This line checks if the value of `$pid` is not `-1`. If it is not `-1`, it means that the child process was created successfully.

4. `pcntl_wait($status);` - This line is used to protect against Zombie children. It waits for the child process to finish execution before continuing with the parent process.

## Helpful links

- [PHP: pcntl_fork - Manual](https://www.php.net/manual/en/function.pcntl-fork.php)
- [PHP: pcntl_wait - Manual](https://www.php.net/manual/en/function.pcntl-wait.php)

onelinerhub: [How to use the PCNTL_FORK function in PHP?](https://onelinerhub.com/php-pcntl/how-to-use-the-pcntl_fork-function-in-php)