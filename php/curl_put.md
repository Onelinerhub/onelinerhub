# Send PUT curl request

```php
$c = curl_init();
curl_setopt($c, CURLOPT_CUSTOMREQUEST, 'PUT');
```

- curl_init - create curl handler
- curl_setopt - sets option for curl handler
- CURLOPT_CUSTOMREQUEST - sets custom request type

group: curl_custom
