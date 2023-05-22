# How to use OpenAI ChatGPT API with PHP?
// plain

OpenAI ChatGPT API can be used with PHP to create natural language processing applications.

## Example code

```php
<?php
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://api.openai.com/v1/engines/chatbot/completions",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 0,
  CURLOPT_FOLLOWLOCATION => true,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS =>"{\n  \"prompt\": \"Hello, how are you?\",\n  \"temperature\": 0.7,\n  \"max_tokens\": 50\n}",
  CURLOPT_HTTPHEADER => array(
    "Content-Type: application/json",
    "Authorization: Bearer <YOUR_API_KEY>"
  ),
));

$response = curl_exec($curl);

curl_close($curl);
echo $response;
```

## Output example

```
{
  "choices": [
    {
      "text": "I'm doing great, thanks for asking!",
      "index": 0
    }
  ]
}
```

## Code explanation

- `curl_init()`: Initializes a new cURL session
- `curl_setopt_array()`: Sets an array of options for a cURL transfer
- `CURLOPT_URL`: The URL to fetch
- `CURLOPT_RETURNTRANSFER`: TRUE to return the transfer as a string of the return value of curl_exec() instead of outputting it out directly
- `CURLOPT_ENCODING`: The contents of the "Accept-Encoding: " header. This enables decoding of the response
- `CURLOPT_MAXREDIRS`: The maximum amount of HTTP redirections to follow
- `CURLOPT_TIMEOUT`: The maximum number of seconds to allow cURL functions to execute
- `CURLOPT_FOLLOWLOCATION`: TRUE to follow any "Location: " header that the server sends as part of the HTTP header
- `CURLOPT_HTTP_VERSION`: CURL_HTTP_VERSION_1_1 (default) to use HTTP/1.1
- `CURLOPT_CUSTOMREQUEST`: The HTTP request method to use
- `CURLOPT_POSTFIELDS`: The full data to post in a HTTP "POST" operation
- `CURLOPT_HTTPHEADER`: An array of HTTP header fields to set, in the format array('Content-type: text/plain', 'Content-length: 100')
- `curl_exec()`: Performs a cURL session
- `curl_close()`: Closes a cURL session

## Helpful links
- [OpenAI ChatGPT API Documentation](https://openai.com/docs/api-reference/chatbot-api/)
- [PHP cURL Documentation](https://www.php.net/manual/en/book.curl.php)

onelinerhub: [How to use OpenAI ChatGPT API with PHP?](https://onelinerhub.com/php-openai/how-to-use-openai-chatgpt-api-with-php)