# Upload file using curl

```php
$c = curl_init( 'https://example.com/' );
curl_setopt_array($c, [
  CURLOPT_RETURNTRANSFER => 1,
  CURLOPT_POST => 1,
  CURLOPT_POSTFIELDS => ['file' => curl_file_create('/tmp/photo.png')]
]);
echo curl_exec($c);
```

- curl_init( - create curl handler for specified URL
- curl_setopt_array( - configures curl
- CURLOPT_RETURNTRANSFER - will return response to variable rather than print
- CURLOPT_POST - set method type to POST
- CURLOPT_POSTFIELDS - post request body
- 'file' - name of the upload field
- '/tmp/photo.png' - path to local file to upload
- curl_exec( - executes GET request to a specified URL

group: curl
