# How can I set the locale for PHP Faker?
// plain

To set the locale for PHP Faker, you need to use the `Faker\Factory::create()` method. This method takes a locale as its first argument. For example, to set the locale to English:

```
$faker = Faker\Factory::create('en_US');
```

This will create a `$faker` object that you can then use to generate data in the specified locale. For example, to generate a random name in English:

```
$name = $faker->name;
echo $name;
```

## Output example

```
Jacob Johnson
```

The list of available locales can be found here: https://github.com/fzaninotto/Faker#localization.

## Code explanation


- `Faker\Factory::create()`: This method creates a new Faker instance with the specified locale.
- `en_US`: This is the locale code for English.
- `$faker->name`: This is a method of the Faker instance that generates a random name.
- `echo $name`: This prints the generated name to the screen.

onelinerhub: [How can I set the locale for PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-set-the-locale-for-php-faker)