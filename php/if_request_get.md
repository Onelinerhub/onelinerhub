# Detect if request method is GET

```php
$is_get = $_SERVER['REQUEST_METHOD'] == 'GET';
```

- $is_get - will contain ```true``` if GET request has been made
- $_SERVER['REQUEST_METHOD'] system variable with current request type

group: request_method
