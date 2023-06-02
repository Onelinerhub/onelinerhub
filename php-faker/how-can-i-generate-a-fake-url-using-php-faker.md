# How can I generate a fake URL using PHP Faker?
// plain

Using PHP Faker, you can generate a fake URL with the `url()` method. This method takes a parameter of `$scheme` which defines the URL protocol. Here is an example:

```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();

echo $faker->url('http');
```

## Output example

```
http://www.paul.org/
```

The code above:
* `require_once 'vendor/autoload.php';` - loads the Faker library
* `$faker = Faker\Factory::create();` - creates an instance of Faker
* `echo $faker->url('http');` - generates a fake URL with the `url()` method, using the `http` protocol

## Helpful links
* [PHP Faker Documentation](https://github.com/fzaninotto/Faker#formatters)
* [Faker\Generator::url](https://github.com/fzaninotto/Faker/blob/master/src/Faker/Generator.php#L737)

onelinerhub: [How can I generate a fake URL using PHP Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-a-fake-url-using-php-faker)