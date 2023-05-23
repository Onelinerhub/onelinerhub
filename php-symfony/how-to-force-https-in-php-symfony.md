# How to force HTTPS in PHP Symfony?
// plain

To force HTTPS in PHP Symfony, you can use the following code snippet:

```
# app/config/config.yml

# To force HTTPS
framework:
    # ...
    trusted_proxies:
        # ...
    trusted_hosts:
        # ...
    session:
        # ...
        cookie_secure: true
        cookie_httponly: true
    default_locale: en
    # ...
    # Force HTTPS
    # uncomment the following line
    # base_url: https://example.com
```

This code snippet will set the `cookie_secure` and `cookie_httponly` parameters to `true` and set the `base_url` parameter to `https://example.com`. This will ensure that all cookies are sent over HTTPS and that all requests are redirected to HTTPS.

## Code explanation


1. `cookie_secure`: sets the cookie to be sent over HTTPS
2. `cookie_httponly`: sets the cookie to be sent over HTTP only
3. `base_url`: sets the base URL to `https://example.com`

## Helpful links

- [Symfony Documentation - How to Configure Symfony](https://symfony.com/doc/current/configuration.html)
- [Symfony Documentation - How to Configure Security](https://symfony.com/doc/current/security.html)

onelinerhub: [How to force HTTPS in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-force-https-in-php-symfony)