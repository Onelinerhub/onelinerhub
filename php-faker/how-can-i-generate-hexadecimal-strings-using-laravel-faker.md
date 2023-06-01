# How can I generate hexadecimal strings using Laravel Faker?
// plain

You can generate hexadecimal strings using Laravel Faker by calling the `hexColor()` method. This method will generate a random hexadecimal string.

## Example code


```php
$faker = Faker\Factory::create();
$hex = $faker->hexColor();
echo $hex;
```

Example output:

```
#a5c2d7
```

## Code explanation


- `$faker = Faker\Factory::create();` - create an instance of the Faker class
- `$hex = $faker->hexColor();` - call the `hexColor()` method to generate a random hexadecimal string
- `echo $hex;` - output the generated hexadecimal string

## Helpful links

- [Faker Documentation](https://github.com/fzaninotto/Faker#formatters)

onelinerhub: [How can I generate hexadecimal strings using Laravel Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-hexadecimal-strings-using-laravel-faker)