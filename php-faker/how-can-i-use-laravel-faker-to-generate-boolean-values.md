# How can I use Laravel Faker to generate boolean values?
// plain

You can use Laravel Faker to generate boolean values by using the boolean() method.

## Example code

```
$booleanValue = Faker\Factory::create()->boolean();
```

## Output example

```
true
```

The boolean() method generates a random boolean value of either true or false. It takes no parameters.

## Code explanation

- `Faker\Factory::create()` - creates a new Faker\Generator instance
- `boolean()` - generates a random boolean value

## Helpful links
- [Laravel Faker Documentation](https://github.com/fzaninotto/Faker#fakerprovideren_boolean)

onelinerhub: [How can I use Laravel Faker to generate boolean values?](https://onelinerhub.com/php-faker/how-can-i-use-laravel-faker-to-generate-boolean-values)