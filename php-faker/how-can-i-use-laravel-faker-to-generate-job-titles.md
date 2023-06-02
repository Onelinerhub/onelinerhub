# How can I use Laravel Faker to generate job titles?
// plain

Faker is a popular library for generating fake data in Laravel. It can be used to generate job titles for testing and development purposes. For example, to generate a job title, you can use the following code:

```php
$faker = Faker\Factory::create();
$jobTitle = $faker->jobTitle;
echo $jobTitle;
```

The output of this code will be a randomly generated job title, such as "Software Engineer" or "Accountant".

## Code explanation


1. `$faker = Faker\Factory::create();` - This line creates a new Faker instance.
2. `$jobTitle = $faker->jobTitle;` - This line generates a job title.
3. `echo $jobTitle;` - This line prints the generated job title.

## Helpful links

- [Faker Documentation](https://github.com/fzaninotto/Faker#fakerprovideren)
- [Laravel Faker Documentation](https://laravel.com/docs/5.8/seeding#using-model-factories)

onelinerhub: [How can I use Laravel Faker to generate job titles?](https://onelinerhub.com/php-faker/how-can-i-use-laravel-faker-to-generate-job-titles)