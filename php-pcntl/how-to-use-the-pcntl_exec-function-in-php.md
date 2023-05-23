# How to use the PCNTL_EXEC function in PHP?
// plain

The PCNTL_EXEC function in PHP is used to execute a program in the background. It takes the program name and its arguments as parameters.

## Example

```
<?php
$program = '/usr/bin/php';
$args = array('-v');
pcntl_exec($program, $args);
```

## Output example

```
PHP 7.2.10 (cli) (built: Sep 10 2018 13:45:04) ( NTS )
Copyright (c) 1997-2018 The PHP Group
Zend Engine v3.2.0, Copyright (c) 1998-2018 Zend Technologies
```

## Code explanation


1. `$program`: This is a string containing the path to the program to be executed.
2. `$args`: This is an array containing the arguments to be passed to the program.
3. `pcntl_exec()`: This is the function that executes the program. It takes two parameters, the program name and its arguments.

## Helpful links

1. [PHP pcntl_exec() Function](https://www.w3schools.com/php/func_pcntl_exec.asp)
2. [PHP pcntl_exec() Manual](http://php.net/manual/en/function.pcntl-exec.php)

onelinerhub: [How to use the PCNTL_EXEC function in PHP?](https://onelinerhub.com/php-pcntl/how-to-use-the-pcntl_exec-function-in-php)