# parameters

How can I use optional parameters with PHP Faker?
// plain

Optional parameters can be used with PHP Faker to customize the output of the Faker class.

## Example code

```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create('en_US');

// With optional parameters
echo $faker->name('male', true);

// Without optional parameters
echo $faker->name();
```

## Output example

```
Dr. Steven Martinez
Alice Cooper
```
In the example above, the first call to `$faker->name()` includes an optional parameter `male` which sets the gender of the generated name to male. The second parameter `true` sets the `$faker->name()` to return a name with a title, such as Dr. or Mr.

The second call to `$faker->name()` does not include any parameters, so a random name will be generated without a title.

## Code explanation

* `require_once 'vendor/autoload.php';` - This includes the autoloader for the Faker library.
* `$faker = Faker\Factory::create('en_US');` - This creates a new instance of the Faker class, with the locale set to `en_US`.
* `echo $faker->name('male', true);` - This calls the `name()` method of the Faker class, with the `male` parameter set to `true` and the `title` parameter set to `true`. This will generate a male name with a title, such as Dr. or Mr.
* `echo $faker->name();` - This calls the `name()` method of the Faker class without any parameters. This will generate a random name without a title.

## Helpful links
* [PHP Faker Documentation](https://github.com/fzaninotto/Faker#fakerproviderbaseaddress)
* [Faker Generator API Reference](https://github.com/fzaninotto/Faker#fakergenerator)

onelinerhub: [parameters

How can I use optional parameters with PHP Faker?](https://onelinerhub.com/php-faker/parameters--how-can-i-use-optional-parameters-with-php-faker)