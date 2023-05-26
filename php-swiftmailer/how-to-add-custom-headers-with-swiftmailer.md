# How to add custom headers with Swiftmailer?
// plain

Swiftmailer allows you to add custom headers to your emails. To do this, you need to use the `addCustomHeader()` method.

```php
$message->addCustomHeader('X-My-Header', 'My Header Value');
```

This will add a custom header with the name `X-My-Header` and the value `My Header Value` to the email.

The `addCustomHeader()` method takes two parameters:

1. `$name` - The name of the custom header.
2. `$value` - The value of the custom header.

## Helpful links

- [Swiftmailer Documentation](https://swiftmailer.symfony.com/docs/introduction.html)

onelinerhub: [How to add custom headers with Swiftmailer?](https://onelinerhub.com/php-swiftmailer/how-to-add-custom-headers-with-swiftmailer)