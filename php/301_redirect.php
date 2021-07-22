# Make 301 redirect

Replace ```https://google.com/``` with required url to redirect to.

```php
die(header('Location: https://google.com/', true, 301));
```

group: redirects
