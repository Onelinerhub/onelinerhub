# How do I use PHP Faker to generate a question mark?
// plain

PHP Faker is a library that can be used to generate fake data for a variety of purposes. To generate a question mark using PHP Faker, you can use the `?` character. For example:

```
<?php
$faker = Faker\Factory::create();
echo $faker->randomElement(['?', '.']);
```

## Output example
 `?`

In the example code above:

- `$faker = Faker\Factory::create();` creates an instance of the Faker library.
- `echo $faker->randomElement(['?', '.']);` uses the `randomElement()` method to randomly select an element from the array of characters (in this case, either '?' or '.').

For more information, please refer to the [PHP Faker documentation](https://github.com/fzaninotto/Faker#basic-usage).

onelinerhub: [How do I use PHP Faker to generate a question mark?](https://onelinerhub.com/php-faker/how-do-i-use-php-faker-to-generate-a-question-mark)