# php swoole_set_process_name

```php
$process = new Swoole\Process(function($worker) {
  echo "the pid of child process is " . $worker->pid . "\n";
  $worker->write('Hi');

  $worker->name("php_child");

  sleep(100);
}, FALSE, 1);

$process->start();
usleep(100);

echo $process->read();
```

- $worker->pid - output child process PID
