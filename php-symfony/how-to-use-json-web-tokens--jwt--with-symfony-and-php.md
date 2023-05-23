# How to use JSON Web Tokens (JWT) with Symfony and PHP?
// plain

JSON Web Tokens (JWT) can be used with Symfony and PHP to securely authenticate and authorize users.

To use JWT with Symfony and PHP, the LexikJWTAuthenticationBundle can be installed and configured.

```
composer require lexik/jwt-authentication-bundle
```

## Code explanation


1. Configure the bundle in `config/packages/lexik_jwt_authentication.yaml`
2. Create a controller to authenticate users and generate a JWT
3. Create a controller to authorize users using the JWT

## Helpful links

- [LexikJWTAuthenticationBundle](https://github.com/lexik/LexikJWTAuthenticationBundle)
- [JWT Authentication for Symfony](https://knpuniversity.com/screencast/jwt)

onelinerhub: [How to use JSON Web Tokens (JWT) with Symfony and PHP?](https://onelinerhub.com/php-symfony/how-to-use-json-web-tokens--jwt--with-symfony-and-php)