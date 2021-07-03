# Disable notices ("Undefined variable", “Undefined index”, "Undefined offset”...)

```php
error_reporting(E_ALL ^ E_NOTICE);
```

- error_reporting - sets new error reporting level
- E_ALL - report all errors
- ^ E_NOTICE - ignore all notices
