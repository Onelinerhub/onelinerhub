# How to download an image with Guzzle in PHP?
// plain

Using Guzzle in PHP to download an image is easy. Here is an example code block to do so:

```
$client = new GuzzleHttp\Client();
$response = $client->request('GET', 'http://example.com/image.jpg');
$image = $response->getBody();
file_put_contents('image.jpg', $image);
```

This code will download the image from the URL `http://example.com/image.jpg` and save it as `image.jpg` in the same directory.

The code consists of the following parts:

1. `$client = new GuzzleHttp\Client();` - This creates a new Guzzle client.
2. `$response = $client->request('GET', 'http://example.com/image.jpg');` - This sends a GET request to the URL `http://example.com/image.jpg` and stores the response in the `$response` variable.
3. `$image = $response->getBody();` - This extracts the body of the response and stores it in the `$image` variable.
4. `file_put_contents('image.jpg', $image);` - This saves the image data stored in the `$image` variable as `image.jpg` in the same directory.

For more information, see the [Guzzle documentation](http://docs.guzzlephp.org/en/stable/).

onelinerhub: [How to download an image with Guzzle in PHP?](https://onelinerhub.com/php-guzzle/how-to-download-an-image-with-guzzle-in-php)