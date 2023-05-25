# How to post data in PHP Guzzle?
// plain

Posting data in PHP Guzzle is easy and straightforward. The following example code block shows how to post data using Guzzle:

```
$client = new GuzzleHttp\Client();
$response = $client->request('POST', 'http://httpbin.org/post', [
    'form_params' => [
        'field_name' => 'abc',
        'other_field' => '123',
        'nested_field' => [
            'nested' => 'hello'
        ]
    ]
]);
```

The output of the above code will be a response object containing the posted data:

```
{
  "args": {},
  "data": "",
  "files": {},
  "form": {
    "field_name": "abc",
    "nested_field": {
      "nested": "hello"
    },
    "other_field": "123"
  },
  "headers": {
    "Accept": "*/*",
    "Content-Length": "60",
    "Content-Type": "application/x-www-form-urlencoded",
    "Host": "httpbin.org",
    "User-Agent": "GuzzleHttp/6.3.3 curl/7.54.0 PHP/7.2.10"
  },
  "json": null,
  "origin": "203.0.113.2",
  "url": "http://httpbin.org/post"
}
```

The code consists of the following parts:

1. `$client = new GuzzleHttp\Client();` - This creates a new Guzzle client object.

2. `$response = $client->request('POST', 'http://httpbin.org/post', [` - This sends a POST request to the specified URL.

3. `'form_params' => [` - This specifies the form parameters to be sent with the request.

4. `'field_name' => 'abc',` - This is an example of a form parameter.

5. `]);` - This closes the form parameters array and the request method.

For more information about posting data with Guzzle, please refer to the [Guzzle documentation](http://docs.guzzlephp.org/en/stable/quickstart.html#sending-form-fields).

onelinerhub: [How to post data in PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-post-data-in-php-guzzle)