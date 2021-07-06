# Get current URL

```php
$url = 'http' . ($_SERVER['HTTPS'] == 'on' ? 's' : '') . '://' . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'];
```

- $url - will contain current URL
- $_SERVER\['HTTPS'\] == 'on' - if this is `true`, then we have secure HTTPS link
- HTTP_HOST - this will contain current domain
- REQUEST_URI - link path (everything after domain name)
