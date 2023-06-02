# How can I specify a string length when using PHP Faker?
// plain

Using PHP Faker, you can specify the length of a string when generating fake data. The `$faker->lexify()` method allows you to create strings with a specific length.

## Example code

```
$faker = Faker\Factory::create();

$string = $faker->lexify('?????');
echo $string;
```

## Output example

```
yjqjv
```

The code above uses the `$faker->lexify('?????')` method, which creates a 5 character string using the characters `?`, `a-z`, `A-Z` and `0-9`. The number of `?` characters specified in the parameter will set the length of the string.

## Code explanation

- `$faker = Faker\Factory::create();` - creates a Faker instance.
- `$faker->lexify('?????')` - creates a 5 character string using the characters `?`, `a-z`, `A-Z` and `0-9`.
- `echo $string;` - prints the generated string.

## Helpful links
- [PHP Faker Documentation](https://github.com/fzaninotto/Faker#lexify)

onelinerhub: [How can I specify a string length when using PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-specify-a-string-length-when-using-php-faker)