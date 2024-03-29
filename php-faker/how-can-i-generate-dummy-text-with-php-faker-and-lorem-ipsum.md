# How can I generate dummy text with PHP Faker and Lorem Ipsum?
// plain

Using [PHP Faker](https://github.com/fzaninotto/Faker) and [Lorem Ipsum](https://github.com/joshtronic/php-loremipsum) libraries, it is possible to generate dummy text in PHP.

#### Example code

```
<?php

require_once 'vendor/autoload.php';

$faker = Faker\Factory::create();
$lorem = new LoremIpsumGenerator;

// Generate a sentence
echo $faker->sentence;

// Generate a paragraph
echo $lorem->getParagraphs(1);

?>
```

#### Output

```
A small river named "Dudley" runs through it.

Pellentesque ut lacus ac purus bibendum hendrerit. Duis eget erat velit. Quisque gravida orci nec nibh viverra, vel aliquam eros aliquet. Aliquam bibendum pharetra velit, in congue nisl egestas vel.

```

The code above consists of the following parts:

1. `require_once 'vendor/autoload.php';` - This line allows us to use the Faker and Lorem Ipsum libraries.

2. `$faker = Faker\Factory::create();` - This line creates an instance of Faker.

3. `$lorem = new LoremIpsumGenerator;` - This line creates an instance of Lorem Ipsum.

4. `echo $faker->sentence;` - This line prints out a sentence generated by Faker.

5. `echo $lorem->getParagraphs(1);` - This line prints out a paragraph generated by Lorem Ipsum.

## Helpful links

- [PHP Faker](https://github.com/fzaninotto/Faker)
- [Lorem Ipsum](https://github.com/joshtronic/php-loremipsum)

onelinerhub: [How can I generate dummy text with PHP Faker and Lorem Ipsum?](https://onelinerhub.com/php-faker/how-can-i-generate-dummy-text-with-php-faker-and-lorem-ipsum)