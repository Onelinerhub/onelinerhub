# How do I generate a fake date of birth using PHP Faker?
// plain

Using PHP Faker, you can generate a fake date of birth with the following code:

```
// Include Faker
require_once 'vendor/autoload.php';

// Create Faker
$faker = Faker\Factory::create();

// Generate a fake date of birth
$dob = $faker->dateTimeThisCentury->format('Y-m-d');

// Output the date of birth
echo $dob;
```

## Output example

```
1962-01-02
```

The code above includes the following parts:

1. `require_once 'vendor/autoload.php';` - This line includes the Faker library.
2. `$faker = Faker\Factory::create();` - This line creates an instance of Faker.
3. `$dob = $faker->dateTimeThisCentury->format('Y-m-d');` - This line generates a fake date of birth using Faker's `dateTimeThisCentury` method.
4. `echo $dob;` - This line outputs the date of birth.

## Helpful links

- [PHP Faker Documentation](https://github.com/fzaninotto/Faker#formatters)

onelinerhub: [How do I generate a fake date of birth using PHP Faker?](https://onelinerhub.com/php-faker/how-do-i-generate-a-fake-date-of-birth-using-php-faker)