# Read large file line by line

```php
$f = fopen('file.txt', 'r');
while ( ($line = fgets($f)) !== false ) {
  // do something with $line
}
```

- fopen - opens file (creates descriptor)
- file.txt - path to file we want to read
- 'r' - we will only read the file (no writing)
- $line = fgets($f) - get next line from file (while there are any lines left)
