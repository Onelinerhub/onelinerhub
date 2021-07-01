# Convert array to CSV line

```php
$f = fopen('php://memory', 'r+');
fputcsv($f, $arr);
rewind($f);
$csv = rtrim(stream_get_contents($f));
```

- fopen('php://memory' - temporary file-like context in memory
- $arr - array to convert to CSV string
- fputcsv($f - write our ```$arr``` to memory using built-in CSV function
- stream_get_contents($f) - get contents of our memory-file-handler (returns CSV string)
