# How to use pcntl_wifexited in PHP?
// plain

PCNTL_WIFEXITED is a PHP function used to determine whether a child process has terminated normally. It takes the status of the child process as an argument and returns a boolean value.

## Example code

```
<?php
$status = pcntl_wifexited($status);
if ($status) {
    echo "Child process terminated normally";
} else {
    echo "Child process did not terminate normally";
}
```

## Output example

```
Child process terminated normally
```

## Code explanation

- pcntl_wifexited($status): This is the function used to determine whether a child process has terminated normally. It takes the status of the child process as an argument.
- $status: This is the argument passed to the pcntl_wifexited() function. It is the status of the child process.
- if ($status): This is the conditional statement used to check the return value of the pcntl_wifexited() function. If the return value is true, it means that the child process has terminated normally.

## Helpful links
- [PHP pcntl_wifexited() Function](https://www.w3schools.com/php/func_pcntl_wifexited.asp)

onelinerhub: [How to use pcntl_wifexited in PHP?](https://onelinerhub.com/php-pcntl/how-to-use-pcntl_wifexited-in-php)