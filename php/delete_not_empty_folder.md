# Remove a directory that is not empty

### This will work only on Linux:

```php
system('rm -rf — ' . escapeshellarg($dir));
```

- `system` - executes OS command
- `rm -rf` - removes given files and folders
- `escapeshellarg` - safely escapes arguments to pass to a `system` command
- `$dir` - path of the directory to remove


