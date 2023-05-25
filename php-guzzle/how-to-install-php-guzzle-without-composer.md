# How to install PHP Guzzle without Composer?
// plain

Guzzle is a PHP HTTP client that can be used to make HTTP requests. It can be installed without Composer by downloading the source code from [GitHub](https://github.com/guzzle/guzzle).

To install Guzzle without Composer, first download the source code from GitHub and extract it to a directory.

```
$ wget https://github.com/guzzle/guzzle/archive/master.zip
$ unzip master.zip
```

Then, include the autoloader file in your PHP script.

```
require 'guzzle-master/vendor/autoload.php';
```

Finally, create a new Guzzle client instance and make a request.

```
$client = new \GuzzleHttp\Client();
$response = $client->request('GET', 'https://example.com');
```

The output of the request will be a `GuzzleHttp\Psr7\Response` object.

```
object(GuzzleHttp\Psr7\Response)#1 (6) {
  ["reasonPhrase":"GuzzleHttp\Psr7\Response":private]=>
  string(2) "OK"
  ["statusCode":"GuzzleHttp\Psr7\Response":private]=>
  int(200)
  ["headers":"GuzzleHttp\Psr7\Response":private]=>
  array(4) {
    ["date"]=>
    array(1) {
      [0]=>
      string(29) "Mon, 10 Aug 2020 13:45:00 GMT"
    }
    ["server"]=>
    array(1) {
      [0]=>
      string(17) "Apache/2.4.18 (Ubuntu)"
    }
    ["last-modified"]=>
    array(1) {
      [0]=>
      string(29) "Mon, 10 Aug 2020 13:45:00 GMT"
    }
    ["content-type"]=>
    array(1) {
      [0]=>
      string(24) "text/html; charset=UTF-8"
    }
  }
  ["headerNames":"GuzzleHttp\Psr7\Response":private]=>
  array(4) {
    ["date"]=>
    string(4) "Date"
    ["server"]=>
    string(6) "Server"
    ["last-modified"]=>
    string(13) "Last-Modified"
    ["content-type"]=>
    string(12) "Content-Type"
  }
  ["protocol":"GuzzleHttp\Psr7\Response":private]=>
  string(3) "1.1"
  ["stream":"GuzzleHttp\Psr7\Response":private]=>
  object(GuzzleHttp\Psr7\Stream)#2 (7) {
    ["stream":"GuzzleHttp\Psr7\Stream":private]=>
    resource(25) of type (stream)
    ["size":"GuzzleHttp\Psr7\Stream":private]=>
    NULL
    ["seekable":"GuzzleHttp\Psr7\Stream":private]=>
    bool(true)
    ["readable":"GuzzleHttp\Psr7\Stream":private]=>
    bool(true)
    ["writable":"GuzzleHttp\Psr7\Stream":private]=>
    bool(true)
    ["uri":"GuzzleHttp\Psr7\Stream":private]=>
    string(10) "php://temp"
    ["customMetadata":"GuzzleHttp\Psr7\Stream":private]=>
    array(0) {
    }
  }
}
```

For more information, see the [Guzzle documentation](http://docs.guzzlephp.org/en/stable/).

onelinerhub: [How to install PHP Guzzle without Composer?](https://onelinerhub.com/php-guzzle/how-to-install-php-guzzle-without-composer)