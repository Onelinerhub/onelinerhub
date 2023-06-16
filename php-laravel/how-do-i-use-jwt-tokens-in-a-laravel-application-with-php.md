# How do I use JWT tokens in a Laravel application with PHP?
// plain

JWT tokens can be used in a Laravel application with PHP to authenticate and authorize users.

To use JWT tokens, you need to install the `tymon/jwt-auth` package. This package provides a set of PHP classes and methods to manage JWT tokens.

Once the package is installed, you can use the `JWTAuth` facade to generate, validate, and refresh tokens.

For example, to generate a token:
```
$token = JWTAuth::attempt($credentials);
```

To validate a token:
```
$user = JWTAuth::authenticate($token);
```

To refresh a token:
```
$newToken = JWTAuth::refresh($token);
```

You can also use the `JWTFactory` facade to create custom tokens with claims.

For example, to create a token with a custom claim:
```
$customClaims = ['name' => 'John Doe'];

$token = JWTFactory::make($customClaims);
```

## Helpful links

- [tymon/jwt-auth package](https://github.com/tymondesigns/jwt-auth)
- [Laravel JWT Authentication Tutorial](https://www.cloudways.com/blog/jwt-authentication-in-laravel/)

onelinerhub: [How do I use JWT tokens in a Laravel application with PHP?](https://onelinerhub.com/php-laravel/how-do-i-use-jwt-tokens-in-a-laravel-application-with-php)