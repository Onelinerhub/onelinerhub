# How to get the process ID with PHP PCNTL?
// plain

The process ID (PID) of a process can be obtained using the `pcntl_getmypid()` function in PHP PCNTL. This function returns the PID of the current process.

## Example code

```
<?php
$pid = pcntl_getmypid();
echo "Process ID: $pid\n";
```

## Output example

```
Process ID: 1234
```

## Code explanation

- `pcntl_getmypid()`: This function returns the PID of the current process.

## Helpful links
- [PHP PCNTL Documentation](https://www.php.net/manual/en/book.pcntl.php)

onelinerhub: [How to get the process ID with PHP PCNTL?](https://onelinerhub.com/php-pcntl/how-to-get-the-process-id-with-php-pcntl)