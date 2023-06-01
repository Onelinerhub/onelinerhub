# How can I generate a fake company name using Laravel Faker?
// plain

Using Laravel Faker, you can easily generate a fake company name.

## Example code

```
$faker = Faker\Factory::create();
$companyName = $faker->company;
echo $companyName;
```
## Output example

```
Jaskolski-Bergstrom
```

The code above creates an instance of the Faker class using the create() method, and then uses the company property of the Faker class to generate a fake company name.

## Code explanation


1. `$faker = Faker\Factory::create();` creates an instance of the Faker class.
2. `$companyName = $faker->company;` uses the company property of the Faker class to generate a fake company name.
3. `echo $companyName;` outputs the fake company name.

## Helpful links

- [Laravel Faker Documentation](https://github.com/fzaninotto/Faker#fakerprovidercompany)

onelinerhub: [How can I generate a fake company name using Laravel Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-a-fake-company-name-using-laravel-faker)