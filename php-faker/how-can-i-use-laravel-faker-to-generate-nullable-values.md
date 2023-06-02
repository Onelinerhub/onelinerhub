# How can I use Laravel Faker to generate nullable values?
// plain

Laravel Faker provides a convenient way to generate random nullable values. The `optional` method of the Faker class can be used to generate a random nullable value.

The `optional` method takes two parameters, the first one being a function that returns the value, and the second one being a probability that the value will be generated.

## Example code

```
$nullableValue = Faker::optional(0.5, function () {
    return Faker::name;
});
```

The above code will generate a random name with a probability of 50%. If the probability is not met, the `$nullableValue` will be `null`.

## Code explanation


- `Faker::optional`: This is the method that is used to generate a random nullable value.
- `0.5`: This is the probability that the value will be generated.
- `Faker::name`: This is the function that returns the value.

## Helpful links

- [Laravel Faker Documentation](https://github.com/fzaninotto/Faker#fakeroptional)

onelinerhub: [How can I use Laravel Faker to generate nullable values?](https://onelinerhub.com/php-faker/how-can-i-use-laravel-faker-to-generate-nullable-values)