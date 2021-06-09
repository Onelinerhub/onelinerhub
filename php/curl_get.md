# Request a URL with curl

```php
$c = curl_init( 'https://example.com/' );
curl_setopt_array($c, [ CURLOPT_RETURNTRANSFER => 1 ]);
echo curl_exec($c);
```

- curl_init( - create curl handler for specified URL
- curl_setopt_array( - configures curl
- CURLOPT_RETURNTRANSFER - will return response to variable rather than print
- curl_exec( - executes GET request to a specified URL

group: curl
