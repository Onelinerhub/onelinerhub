# How to use PCNTL alarm in PHP?
// plain

PCNTL (Process Control) is a PHP extension that allows you to execute Unix-like process control functions in PHP. The `pcntl_alarm()` function is used to set an alarm signal after a specified time interval.

```
<?php
// Set an alarm to go off in 5 seconds
pcntl_alarm(5);

// Do some processing
echo "Doing some processing...\n";
sleep(10);

echo "Done!\n";
?>
```

## Output example

```
Doing some processing...
Done!
```

The code above sets an alarm to go off in 5 seconds and then does some processing. After the alarm is triggered, the script will terminate.

## Code explanation

- `pcntl_alarm(5)`: Sets an alarm to go off in 5 seconds.
- `echo "Doing some processing...\n"`: Prints a message to the screen.
- `sleep(10)`: Pauses the script for 10 seconds.
- `echo "Done!\n"`: Prints a message to the screen.

## Helpful links
- [PHP PCNTL Manual](https://www.php.net/manual/en/ref.pcntl.php)
- [PHP pcntl_alarm() Function](https://www.w3schools.com/php/func_pcntl_alarm.asp)

onelinerhub: [How to use PCNTL alarm in PHP?](https://onelinerhub.com/php-pcntl/how-to-use-pcntl-alarm-in-php)