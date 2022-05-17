# How to measure execution time

```php
$start = time();
# Other code:
sleep(15);
$time = time() - $start;
```

- ```$start = time();``` - assign the current time to a variable called ``$start``
- ```# Other code``` - the rest of the code to execute
- ```sleep(15);``` - wait 15 seconds (for testing purposes)
- ```$time = time() - $start;``` - assign the total time since ``$start`` to a variable called ``$time``

## Example: 
```php
$start = time();
sleep(15);
$time = time() - $start;
echo $time . " seconds";

```
```
15 seconds

```

