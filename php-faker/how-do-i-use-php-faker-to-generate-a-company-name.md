# How do I use PHP Faker to generate a company name?
// plain

PHP Faker is a library that provides a set of tools for generating fake data such as names, addresses, and phone numbers. It can also be used to generate a company name. To generate a company name with PHP Faker, you need to first install the library.

```
composer require fzaninotto/faker
```

Once installed, you can use the `Company` class to generate a company name.

```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

echo $faker->company;
```

## Output example

```
Smith-Mills
```

The code above includes the following parts:

1. `require_once 'vendor/autoload.php';` - This line includes the autoloader file which is used to load the Faker library.

2. `$faker = Faker\Factory::create();` - This line creates an instance of the Faker library.

3. `echo $faker->company;` - This line generates a company name.

For more information on using the Faker library, please refer to the [official documentation](https://github.com/fzaninotto/Faker#fakerprovidecompany).

onelinerhub: [How do I use PHP Faker to generate a company name?](https://onelinerhub.com/php-faker/how-do-i-use-php-faker-to-generate-a-company-name)