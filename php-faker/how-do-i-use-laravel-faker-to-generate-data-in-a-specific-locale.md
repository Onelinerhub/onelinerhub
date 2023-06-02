# How do I use Laravel Faker to generate data in a specific locale?
// plain

To use Laravel Faker to generate data in a specific locale, you can use the following code:

```
$faker = Faker\Factory::create('es_ES');
```

This will create an instance of Faker using the Spanish locale. The locale is specified in the ISO 639-1 format, with an optional region code, e.g. `es_ES` for Spanish in Spain.

You can then use the `$faker` instance to generate data in the specified locale. For example, to generate a name:

```
echo $faker->name;
```

## Output example

```
María García
```

The code consists of two parts:

1. `Faker\Factory::create('es_ES')`: This creates an instance of Faker using the Spanish locale.
2. `$faker->name`: This uses the `$faker` instance to generate a name.

For more information, see the [Laravel Faker documentation](https://github.com/fzaninotto/Faker#localization).

onelinerhub: [How do I use Laravel Faker to generate data in a specific locale?](https://onelinerhub.com/php-faker/how-do-i-use-laravel-faker-to-generate-data-in-a-specific-locale)