# Set process name

```php
$prc = new Swoole\Process(function($worker) {
  echo "Child PID " . $worker->pid . "\n";

  $worker->name('php_child');

  sleep(100);
}, FALSE, 1);

$prc->start();
usleep(100);
echo "\n";
```

- $worker->pid - output child process PID
- $worker->name - rename child process
- ->start() - start process (this will start child process in background)
- usleep(100) - wait for some time to make sure child process have started


## Example
```php
php process.php

```
```ps a | grep php_child
1078572 pts/2    S      0:00 php_child```