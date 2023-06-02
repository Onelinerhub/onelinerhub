# How can I generate a unique ID using PHP Faker?
// plain

Using PHP Faker, you can generate a unique ID with the following code snippet:

```
<?php
// include the Faker library
require_once 'vendor/fzaninotto/faker/src/autoload.php';

// create a Faker object
$faker = Faker\Factory::create();

// generate a unique ID
$unique_id = $faker->uuid;

echo $unique_id;
```

## Output example
 `d1f08a3d-9e8b-4f9d-b9c8-0d6f7d7c3c9a`

The code above includes the following parts:

1. `require_once 'vendor/fzaninotto/faker/src/autoload.php';` - this line includes the Faker library.

2. `$faker = Faker\Factory::create();` - this line creates a Faker object.

3. `$unique_id = $faker->uuid;` - this line generates a unique ID.

4. `echo $unique_id;` - this line prints the generated unique ID.

## Helpful links

- [Faker Documentation](https://github.com/fzaninotto/Faker)
- [PHP Faker](https://github.com/fzaninotto/Faker#usage)

onelinerhub: [How can I generate a unique ID using PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-a-unique-id-using-php-faker)