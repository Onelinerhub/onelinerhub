# How can I generate fake birthdays using Laravel Faker?
// plain

Using [Laravel Faker](https://github.com/fzaninotto/Faker) you can generate fake birthdays with ease. Here is an example code block to generate a fake birthday and the output of that code:

```
$faker = Faker\Factory::create();
$birthday = $faker->dateTimeBetween('-50 years', 'now');
echo $birthday->format('Y-m-d');
```

## Output example
 `1990-02-25`

The code is composed of the following parts:

1. `$faker = Faker\Factory::create();` - This creates a new Faker instance.
2. `$birthday = $faker->dateTimeBetween('-50 years', 'now');` - This creates a random datetime object between the range of 50 years ago and now.
3. `echo $birthday->format('Y-m-d');` - This prints out the birthday in the format of Y-m-d.

You can also customize the range of the generated birthdays by changing the parameters of `dateTimeBetween()`. For more information, refer to the [Faker documentation](https://github.com/fzaninotto/Faker#fakerproviderdatedatetime).

onelinerhub: [How can I generate fake birthdays using Laravel Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-fake-birthdays-using-laravel-faker)