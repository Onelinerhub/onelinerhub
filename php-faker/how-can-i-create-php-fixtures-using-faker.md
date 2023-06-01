# How can I create PHP fixtures using Faker?
// plain

Creating PHP fixtures using Faker is a great way to quickly generate test data. Faker is a PHP library that generates fake data for you. Here is an example of how to create a fixture with Faker:

```php
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

$fixture = [
  'name' => $faker->name,
  'email' => $faker->email,
  'address' => $faker->address,
];

print_r($fixture);
```

## Output example


```
Array
(
    [name] => Mrs. Rachelle Kunze
    [email] => mauricio_kilback@hotmail.com
    [address] => 05848 Bogan Stravenue
    Apt. 925
    New Travon, WI 54515
)
```

The code above will generate a fixture containing a name, email address, and address. The `require_once` statement is used to include the Faker library. The `$faker` variable is then used to create an instance of the Faker library. The `$fixture` array is then populated with fake data generated from the `$faker` instance. Finally, the `print_r` statement is used to output the fixture to the screen.

## Helpful links
* [Faker PHP Library](https://github.com/fzaninotto/Faker)

onelinerhub: [How can I create PHP fixtures using Faker?](https://onelinerhub.com/php-faker/how-can-i-create-php-fixtures-using-faker)