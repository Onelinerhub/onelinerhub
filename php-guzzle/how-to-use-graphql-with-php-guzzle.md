# How to use GraphQL with PHP Guzzle?
// plain

GraphQL can be used with PHP Guzzle to make HTTP requests to a GraphQL endpoint.

## Example code

```
$client = new \GuzzleHttp\Client();
$response = $client->post('http://example.com/graphql', [
    'json' => [
        'query' => '{ hello }'
    ]
]);
```

## Output example

```
{
    "data": {
        "hello": "world"
    }
}
```

## Code explanation

- `$client = new \GuzzleHttp\Client();` - creates a new Guzzle client
- `$response = $client->post('http://example.com/graphql', [` - makes a POST request to the GraphQL endpoint
- `'json' => [` - sets the request body to JSON
- `'query' => '{ hello }'` - sets the GraphQL query

## Helpful links
- [Guzzle Documentation](http://docs.guzzlephp.org/en/stable/)
- [GraphQL Documentation](https://graphql.org/learn/)

onelinerhub: [How to use GraphQL with PHP Guzzle?](https://onelinerhub.com/php-guzzle/how-to-use-graphql-with-php-guzzle)