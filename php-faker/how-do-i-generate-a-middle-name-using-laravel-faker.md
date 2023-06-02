# How do I generate a middle name using Laravel Faker?
// plain

Generating a middle name using Laravel Faker is fairly straightforward.

First, you'll need to install the Faker package. This can be done with the following command:
```
composer require fzaninotto/faker
```

Once that's done, you can use the following example code to generate a middle name:

```
use Faker\Generator as Faker;

$faker = Faker::create();

echo $faker->name('middleName');
```

This will output a randomly generated middle name, for example:

```
Jacob
```

## Code explanation


* `use Faker\Generator as Faker;`: This imports the Faker class.
* `$faker = Faker::create();`: This creates an instance of the Faker class.
* `echo $faker->name('middleName');`: This generates a random middle name.

For more information on using Laravel Faker, please see the [official documentation](https://github.com/fzaninotto/Faker#fakerprovidername).

onelinerhub: [How do I generate a middle name using Laravel Faker?](https://onelinerhub.com/php-faker/how-do-i-generate-a-middle-name-using-laravel-faker)