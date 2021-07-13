# Append line to a file

```php
file_put_contents('file.txt', 'some line' . "\n", FILE_APPEND | LOCK_EX);
```

- file_put_contents - writes text to a file
- file.txt - file path to append line to
- 'some line' - text line to append to a file
- "\n" - new line symbol, so our line ends with line break
- FILE_APPEND - flag that asks php to append content rather than overwrite
- LOCK_EX - this will prevent others from writing this file at the same time
