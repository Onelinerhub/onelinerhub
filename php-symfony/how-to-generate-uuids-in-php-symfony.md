# How to generate UUIDs in PHP Symfony?
// plain

UUIDs (Universally Unique Identifiers) can be generated in PHP Symfony using the `Ramsey\Uuid\Uuid` class.

## Example code

```
use Ramsey\Uuid\Uuid;

$uuid4 = Uuid::uuid4();
echo $uuid4->toString();
```

## Output example

```
f3c9c2f2-f9f2-4f1f-b9f2-9f2f3f2f3f2f
```

## Code explanation

- `use Ramsey\Uuid\Uuid;` - imports the `Uuid` class from the `Ramsey\Uuid` namespace
- `Uuid::uuid4()` - generates a version 4 (random) UUID
- `$uuid4->toString()` - returns the UUID as a string

## Helpful links
- [Ramsey UUID documentation](https://packagist.org/packages/ramsey/uuid)

onelinerhub: [How to generate UUIDs in PHP Symfony?](https://onelinerhub.com/php-symfony/how-to-generate-uuids-in-php-symfony)