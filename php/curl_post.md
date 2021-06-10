# Make a POST request with curl

```php
$c = curl_init( 'https://example.com/' );
curl_setopt_array($c, [
  CURLOPT_RETURNTRANSFER => 1,
  CURLOPT_POST => 1,
  CURLOPT_POSTFIELDS => http_build_query(['a' => 1, 'b' => 2])
]);
echo curl_exec($c);
```

- curl_init( - create curl handler for specified URL
- curl_setopt_array( - configures curl
- CURLOPT_RETURNTRANSFER - will return response to variable rather than print
- CURLOPT_POST - set method type to POST
- CURLOPT_POSTFIELDS - post request body
- http_build_query - build post body from specified array of variables and values
- curl_exec( - executes GET request to a specified URL

group: curl
