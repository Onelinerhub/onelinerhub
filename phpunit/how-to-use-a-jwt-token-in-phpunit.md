# How to use a JWT token in PHPUnit?
// plain

Using a JWT token in PHPUnit is a great way to test the authentication of an API.

```
<?php

// Create a JWT token
$token = JWT::encode($payload, $key);

// Set the token in the header
$headers = array('Authorization' => 'Bearer ' . $token);

// Make the request
$response = $client->request('GET', '/api/endpoint', [], [], $headers);

// Assert the response
$this->assertEquals(200, $response->getStatusCode());
```

The example code above shows how to create a JWT token, set it in the header, make a request, and assert the response.

## Code explanation


1. Create a JWT token: `$token = JWT::encode($payload, $key);`
2. Set the token in the header: `$headers = array('Authorization' => 'Bearer ' . $token);`
3. Make the request: `$response = $client->request('GET', '/api/endpoint', [], [], $headers);`
4. Assert the response: `$this->assertEquals(200, $response->getStatusCode());`

## Helpful links

- [JWT Authentication for PHP](https://jwt.io/introduction/)
- [PHPUnit Documentation](https://phpunit.readthedocs.io/en/latest/)

onelinerhub: [How to use a JWT token in PHPUnit?](https://onelinerhub.com/phpunit/how-to-use-a-jwt-token-in-phpunit)