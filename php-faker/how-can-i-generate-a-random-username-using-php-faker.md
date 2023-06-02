# How can I generate a random username using PHP Faker?
// plain

Using [PHP Faker](https://github.com/fzaninotto/Faker), you can generate a random username by combining random words from the Faker library.

## Example code


```php
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

$username = $faker->word . '_' . $faker->word;

echo $username;

```

## Output example


```
satisfied_vacation
```

The code above will generate a random username by combining two random words from the Faker library. The `require_once` line includes the Faker library. The `$faker` line creates a Faker instance. The `$username` line combines two random words from the Faker library with an underscore separator. The `echo` line prints the random username.

## Helpful links

- [Faker GitHub page](https://github.com/fzaninotto/Faker)
- [Faker documentation](https://github.com/fzaninotto/Faker#fakerproviderword)

onelinerhub: [How can I generate a random username using PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-a-random-username-using-php-faker)