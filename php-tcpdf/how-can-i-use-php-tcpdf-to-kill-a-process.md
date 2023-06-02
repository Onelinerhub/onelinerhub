# How can I use PHP TCPDF to kill a process?
// plain

Using PHP TCPDF, it is not possible to kill a process directly. However, it is possible to execute system commands from a PHP script and then use those commands to kill a process.

For example, the following code block can be used to kill a process with the ID of 1234:

```
<?php
exec('kill 1234');
?>
```

This code will not produce any output.

The code consists of two parts:
1. The `exec()` function which executes a system command.
2. The `kill` command which terminates the process with the ID specified.

For more information, see the following links:
- [PHP exec()](https://www.php.net/manual/en/function.exec.php)
- [Linux kill command](https://linux.die.net/man/1/kill)

onelinerhub: [How can I use PHP TCPDF to kill a process?](https://onelinerhub.com/php-tcpdf/how-can-i-use-php-tcpdf-to-kill-a-process)