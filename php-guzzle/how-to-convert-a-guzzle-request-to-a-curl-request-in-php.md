# How to convert a Guzzle request to a cURL request in PHP?
// plain

Converting a Guzzle request to a cURL request in PHP is relatively straightforward. The following example code block shows how to do this:
```
$client = new GuzzleHttp\Client();
$res = $client->request('GET', 'http://www.example.com');

$curl = curl_init();
curl_setopt_array($curl, array(
    CURLOPT_URL => "http://www.example.com",
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_ENCODING => "",
    CURLOPT_MAXREDIRS => 10,
    CURLOPT_TIMEOUT => 30,
    CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
    CURLOPT_CUSTOMREQUEST => "GET",
    CURLOPT_HTTPHEADER => array(
        "cache-control: no-cache"
    ),
));

$response = curl_exec($curl);
$err = curl_error($curl);

curl_close($curl);

if ($err) {
    echo "cURL Error #:" . $err;
} else {
    echo $response;
}
```

## Code explanation


- `$client = new GuzzleHttp\Client();`: This line creates a new Guzzle client.
- `$res = $client->request('GET', 'http://www.example.com');`: This line sends a GET request to the specified URL.
- `$curl = curl_init();`: This line initializes a cURL session.
- `curl_setopt_array($curl, array(`: This line sets the cURL options.
- `CURLOPT_URL => "http://www.example.com",`: This line sets the URL for the cURL request.
- `CURLOPT_RETURNTRANSFER => true,`: This line sets the cURL request to return the response instead of outputting it.
- `CURLOPT_ENCODING => "",`: This line sets the encoding for the cURL request.
- `CURLOPT_MAXREDIRS => 10,`: This line sets the maximum number of redirects for the cURL request.
- `CURLOPT_TIMEOUT => 30,`: This line sets the timeout for the cURL request.
- `CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,`: This line sets the HTTP version for the cURL request.
- `CURLOPT_CUSTOMREQUEST => "GET",`: This line sets the request method for the cURL request.
- `CURLOPT_HTTPHEADER => array(`: This line sets the HTTP headers for the cURL request.
- `"cache-control: no-cache"`: This line sets the cache control header for the cURL request.
- `$response = curl_exec($curl);`: This line executes the cURL request.
- `$err = curl_error($curl);`: This line checks for any errors in the cURL request.
- `curl_close($curl);`: This line closes the cURL session.
- `if ($err) {`: This line checks if there were any errors in the cURL request.
- `echo "cURL Error #:" . $err;`: This line outputs the error message.
- `} else {`: This line checks if there were no errors in the cURL request.
- `echo $response;`: This line outputs the response from the cURL request.

## Helpful links

- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [cURL Documentation](https://curl.haxx.se/libcurl/c/libcurl.html)

onelinerhub: [How to convert a Guzzle request to a cURL request in PHP?](https://onelinerhub.com/php-guzzle/how-to-convert-a-guzzle-request-to-a-curl-request-in-php)