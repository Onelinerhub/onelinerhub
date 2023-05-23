# How to use GraphQL with PHP Symfony?
// plain

GraphQL can be used with PHP Symfony by installing the [webonyx/graphql-php](https://github.com/webonyx/graphql-php) library.

## Example code

```php
use GraphQL\Type\Definition\ObjectType;
use GraphQL\Type\Definition\Type;

$queryType = new ObjectType([
    'name' => 'Query',
    'fields' => [
        'hello' => [
            'type' => Type::string(),
            'resolve' => function () {
                return 'Hello world!';
            }
        ]
    ]
]);
```

## Output example

```
Hello world!
```

The code above creates a `Query` object type with a `hello` field that returns a string `Hello world!`.

## Helpful links
- [webonyx/graphql-php](https://github.com/webonyx/graphql-php)
- [GraphQL with Symfony](https://www.webonyx.com/graphql/php/symfony)

onelinerhub: [How to use GraphQL with PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-use-graphql-with-php-symfony)