# How do I generate a fake IBAN using PHP Faker?
// plain

Using the [PHP Faker](https://github.com/fzaninotto/Faker) library, you can generate a fake IBAN with the following code:

```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

echo $faker->iban();

```

## Output example


```
TR970020500171797650307526
```

The code is composed of the following parts:

1. `require_once 'vendor/autoload.php'`: This is used to include the Faker library in the code.
2. `$faker = Faker\Factory::create()`: This creates an instance of the Faker library.
3. `echo $faker->iban()`: This generates a fake IBAN and prints it out.

## Helpful links

- [PHP Faker](https://github.com/fzaninotto/Faker)
- [IBAN Format](https://www.iban.com/structure)

onelinerhub: [How do I generate a fake IBAN using PHP Faker?](https://onelinerhub.com/php-faker/how-do-i-generate-a-fake-iban-using-php-faker)