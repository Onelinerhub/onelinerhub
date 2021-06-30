# Enable errors display

```php
ini_set('display_errors', 1);
ini_set('display_startup_errors', 1);
error_reporting(E_ALL);
```

- display_errors - print all errors right into output
- display_startup_errors - will also print fatal errors during php startup
- error_reporting(E_ALL) - this will ask PHP to display all types of errors

group: errors
