# How to use OpenAI API with PHP?
// plain

OpenAI API can be used with PHP by using the [OpenAI PHP SDK](https://github.com/openai/openai-php-sdk).

## Example code

```php
<?php
require_once __DIR__ . '/vendor/autoload.php';

$openai = new \OpenAI\Client('<your-api-key>', '<your-api-secret>');
$response = $openai->engines->create('davinci', ['temperature' => 0.5]);

echo $response->body->id;
```

## Output example

```
davinci_abc123
```

## Code explanation


- `require_once __DIR__ . '/vendor/autoload.php';`: This line includes the autoloader for the OpenAI SDK.
- `$openai = new \OpenAI\Client('<your-api-key>', '<your-api-secret>');`: This line creates a new OpenAI client object with your API key and secret.
- `$response = $openai->engines->create('davinci', ['temperature' => 0.5]);`: This line creates a new engine with the given parameters.
- `echo $response->body->id;`: This line prints out the ID of the newly created engine.

## Helpful links

- [OpenAI PHP SDK](https://github.com/openai/openai-php-sdk)
- [OpenAI API Documentation](https://openai.com/docs/api-reference)

onelinerhub: [How to use OpenAI API with PHP?](https://onelinerhub.com/php-openai/how-to-use-openai-api-with-php)