# How to use OpenAI API and PHP and cURL?
// plain

OpenAI API can be used with PHP and cURL to access the OpenAI API. The following example code shows how to use cURL to make a request to the OpenAI API:

```
$curl = curl_init();

curl_setopt_array($curl, array(
  CURLOPT_URL => "https://api.openai.com/v1/engines/davinci/completions",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_ENCODING => "",
  CURLOPT_MAXREDIRS => 10,
  CURLOPT_TIMEOUT => 30,
  CURLOPT_HTTP_VERSION => CURL_HTTP_VERSION_1_1,
  CURLOPT_CUSTOMREQUEST => "POST",
  CURLOPT_POSTFIELDS => "{\n  \"prompt\": \"The quick brown fox\",\n  \"max_tokens\": 50\n}",
  CURLOPT_HTTPHEADER => array(
    "Authorization: Bearer <YOUR_API_KEY>",
    "Content-Type: application/json"
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

The output of the example code will be a JSON response from the OpenAI API.

## Code explanation


1. `$curl = curl_init();` - Initializes a cURL session.
2. `curl_setopt_array($curl, array(` - Sets the options for the cURL session.
3. `CURLOPT_URL => "https://api.openai.com/v1/engines/davinci/completions",` - Sets the URL for the cURL request.
4. `CURLOPT_POSTFIELDS => "{\n  \"prompt\": \"The quick brown fox\",\n  \"max_tokens\": 50\n}",` - Sets the POST fields for the cURL request.
5. `CURLOPT_HTTPHEADER => array(` - Sets the HTTP headers for the cURL request.
6. `"Authorization: Bearer <YOUR_API_KEY>",` - Sets the authorization header for the cURL request.
7. `"Content-Type: application/json"` - Sets the content type header for the cURL request.
8. `$response = curl_exec($curl);` - Executes the cURL request.
9. `$err = curl_error($curl);` - Checks for any errors in the cURL request.
10. `curl_close($curl);` - Closes the cURL session.
11. `if ($err) {` - Checks if there were any errors in the cURL request.
12. `echo "cURL Error #:" . $err;` - Prints out the error message.
13. `echo $response;` - Prints out the response from the OpenAI API.

## Helpful links

- [OpenAI API Documentation](https://openai.com/docs/api-overview/)
- [PHP cURL Documentation](https://www.php.net/manual/en/book.curl.php)

onelinerhub: [How to use OpenAI API and PHP and cURL?](https://onelinerhub.com/php-openai/how-to-use-openai-api-and-php-and-curl)