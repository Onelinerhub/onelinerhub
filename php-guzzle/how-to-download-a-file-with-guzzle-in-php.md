# How to download a file with Guzzle in PHP?
// plain

Using Guzzle in PHP to download a file is easy. Here is an example code block to demonstrate how to do it:

```
<?php
$client = new GuzzleHttp\Client();
$response = $client->request('GET', 'http://example.com/file.zip', [
    'sink' => '/path/to/file.zip'
]);
```

This code will download the file from `http://example.com/file.zip` and save it to `/path/to/file.zip`.

The code consists of the following parts:

1. `$client = new GuzzleHttp\Client();` - creates a new Guzzle client.
2. `$response = $client->request('GET', 'http://example.com/file.zip', [` - sends a GET request to the specified URL.
3. `'sink' => '/path/to/file.zip'` - specifies the path to save the file to.
4. `]);` - closes the array of options.

For more information, please refer to the [Guzzle documentation](http://docs.guzzlephp.org/en/stable/).

onelinerhub: [How to download a file with Guzzle in PHP?](https://onelinerhub.com/php-guzzle/how-to-download-a-file-with-guzzle-in-php)