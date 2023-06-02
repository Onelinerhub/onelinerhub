# How do I generate a list of fake data using Laravel Faker?
// plain

Using the [Laravel Faker](https://github.com/fzaninotto/Faker) library, you can generate a list of fake data. Here is an example code block to generate a list of 10 fake names:

```
<?php

use Faker\Factory as Faker;

$faker = Faker::create();

for ($i = 0; $i < 10; $i++) {
    echo $faker->name . "\n";
}
```

The output of this code block will be a list of 10 fake names, such as:

```
John Smith
Anna Jones
Sarah Brown
Mark Wilson
Steven Johnson
Karen Williams
Daniel Miller
Elizabeth Davis
Brian Anderson
David Taylor
```

The code block consists of the following parts:
1. `use Faker\Factory as Faker;`: This line imports the Faker library.
2. `$faker = Faker::create();`: This line creates an instance of the Faker class.
3. `for ($i = 0; $i < 10; $i++)`: This is a for loop that will execute 10 times.
4. `echo $faker->name . "\n";`: This line prints out a fake name and adds a new line character.

You can use the Faker library to generate a variety of fake data, such as addresses, phone numbers, emails, etc. You can find the full list of available options in the [Faker documentation](https://github.com/fzaninotto/Faker#formatters).

onelinerhub: [How do I generate a list of fake data using Laravel Faker?](https://onelinerhub.com/php-faker/how-do-i-generate-a-list-of-fake-data-using-laravel-faker)