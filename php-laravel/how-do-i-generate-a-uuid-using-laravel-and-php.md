# How do I generate a UUID using Laravel and PHP?
// plain

UUID stands for Universally Unique Identifier and is a 128-bit number used to identify information in computer systems. In Laravel and PHP, UUIDs can be generated using the `Ramsey\Uuid\Uuid` class.

## Example code

```
use Ramsey\Uuid\Uuid;

$uuid = Uuid::uuid4();
echo $uuid->toString();
```

## Output example

```
d6e3c3d8-e7b3-4caf-8c3f-7bb3b881b863
```

## Code explanation

- `use Ramsey\Uuid\Uuid;` - This line imports the Uuid class from the `ramsey/uuid` package.
- `$uuid = Uuid::uuid4();` - This line generates a version 4 UUID.
- `echo $uuid->toString();` - This line outputs the UUID as a string.

## Helpful links
- [Ramsey UUID Package](https://packagist.org/packages/ramsey/uuid)
- [UUID - Wikipedia](https://en.wikipedia.org/wiki/Universally_unique_identifier)

onelinerhub: [How do I generate a UUID using Laravel and PHP?](https://onelinerhub.com/php-laravel/how-do-i-generate-a-uuid-using-laravel-and-php)