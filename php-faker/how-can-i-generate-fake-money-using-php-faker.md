# How can I generate fake money using PHP Faker?
// plain

Using [PHP Faker](https://github.com/fzaninotto/Faker) library, you can generate fake money using the `randomNumber()` method. The method takes two parameters, the first one being the number of digits and the second one being the number of decimal places. For example, the following code will generate a random number with 10 digits and two decimal places:

```php
$faker = Faker\Factory::create();
echo $faker->randomNumber(10,2);
```

## Output example

```
66.80
```

The code consists of the following parts:

1. `$faker = Faker\Factory::create();` - This initializes the Faker library.
2. `echo $faker->randomNumber(10,2);` - This calls the `randomNumber()` method with two parameters (10 digits and 2 decimal places) and prints the output.

## Helpful links

- [Faker Documentation](https://github.com/fzaninotto/Faker#fakerproviderbasenumber)
- [PHP Faker Library](https://github.com/fzaninotto/Faker)

onelinerhub: [How can I generate fake money using PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-fake-money-using-php-faker)