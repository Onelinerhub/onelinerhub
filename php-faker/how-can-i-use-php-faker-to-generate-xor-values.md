# How can I use PHP Faker to generate XOR values?
// plain

PHP Faker can be used to generate XOR values by using the Faker\Generator::optional() method. This method allows for the generation of a boolean value based on a given probability. The optional() method takes two parameters; the first parameter is the probability for the boolean value to be true, and the second parameter is the probability for the boolean value to be false.

For example, the following code block will generate a random XOR value based on a probability of 0.5 for both true and false values:

```
<?php
$faker = Faker\Factory::create();

$xor = $faker->optional(0.5, 0.5);
echo $xor;
```

## Output example

```
false
```

The code block above contains the following parts:
- The first line creates a new instance of the Faker\Factory class.
- The second line uses the optional() method to generate a boolean value based on a given probability. The first parameter is the probability for the boolean value to be true, and the second parameter is the probability for the boolean value to be false.
- The third line prints the generated XOR value.

## Helpful links
- [Faker\Generator::optional()](https://github.com/fzaninotto/Faker/blob/master/src/Faker/Generator.php#L1428)
- [PHP Faker Documentation](https://github.com/fzaninotto/Faker#fakerprovidername)

onelinerhub: [How can I use PHP Faker to generate XOR values?](https://onelinerhub.com/php-faker/how-can-i-use-php-faker-to-generate-xor-values)