# Create directory recursively

```php
mkdir('/path/to/dir', 0777, true);
```

- mkdir - creates directory
- /path/to/dir - path to the new dir
- 0777 - [mode](/bash/chmod) to create new directory with
- true - this will ask `mkdir` to create all subdirectories in the path if they don't exist
