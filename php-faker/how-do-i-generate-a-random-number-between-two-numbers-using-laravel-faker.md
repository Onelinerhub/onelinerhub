# How do I generate a random number between two numbers using Laravel Faker?
// plain

Using Laravel Faker, you can easily generate a random number between two numbers. To do so, you need to use the `numberBetween()` method. This method takes two arguments, the minimum and maximum number.

For example, to generate a random number between 1 and 10, you can use the following code:
```
$randomNumber = Faker::numberBetween(1, 10);
echo $randomNumber;
```
This will output a random number between 1 and 10, for example `4`.

## Code explanation


1. `$randomNumber =`: This is a variable that will store the generated random number.
2. `Faker::numberBetween(1, 10);`: This is the method that will generate the random number. The `1` and `10` are the arguments that will define the minimum and maximum number.
3. `echo $randomNumber;`: This will output the generated random number.

## Helpful links

- [Laravel Faker Documentation](https://github.com/fzaninotto/Faker#formatters)

onelinerhub: [How do I generate a random number between two numbers using Laravel Faker?](https://onelinerhub.com/php-faker/how-do-i-generate-a-random-number-between-two-numbers-using-laravel-faker)