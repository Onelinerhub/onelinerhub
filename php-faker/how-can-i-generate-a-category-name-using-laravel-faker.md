# How can I generate a category name using Laravel Faker?
// plain

Using Laravel Faker, you can generate a category name with the following code:
```
$faker = Faker\Factory::create();
$categoryName = $faker->word;
```
This will generate a random word that can be used as a category name. For example, it might generate the word "furniture".

## Code explanation

1. `$faker = Faker\Factory::create();`: This creates an instance of the Faker class.
2. `$categoryName = $faker->word;`: This generates a random word that can be used as a category name.

No output is generated.

## Helpful links
- https://github.com/fzaninotto/Faker
- https://laravel.com/docs/7.x/database-testing#generating-fake-data-with-factories

onelinerhub: [How can I generate a category name using Laravel Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-a-category-name-using-laravel-faker)