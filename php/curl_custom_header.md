# Send custom headers using Curl

```php
$c = curl_init();
# ...
curl_setopt($c, CURLOPT_HTTPHEADER, ['X-My-Header: 1', 'Other-header: 2']);
```

- curl_init - create curl handler
- curl_setopt - sets option for curl handler
- CURLOPT_HTTPHEADER - sets custom header
- 'X-My-Header: 1' - first custom header to send
- 'Other-header: 2' - second custom header to send
