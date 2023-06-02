# How can I generate a fake IP address using PHP Faker?
// plain

Using the PHP Faker library, you can generate a fake IP address with the following code:

```
<?php

require_once __DIR__ . '/vendor/autoload.php';

$faker = Faker\Factory::create();

echo $faker->ipv4;

```

## Output example

```
87.84.163.13
```

The code consists of the following parts:

1. `require_once __DIR__ . '/vendor/autoload.php';` - This line includes the vendor autoload file which is needed for the Faker library.

2. `$faker = Faker\Factory::create();` - This line creates a new Faker instance.

3. `echo $faker->ipv4;` - This line prints out the generated fake IP address.

For more information about the PHP Faker library, check out the [documentation](https://github.com/fzaninotto/Faker#fakerprovideren_usaddress).

onelinerhub: [How can I generate a fake IP address using PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-a-fake-ip-address-using-php-faker)