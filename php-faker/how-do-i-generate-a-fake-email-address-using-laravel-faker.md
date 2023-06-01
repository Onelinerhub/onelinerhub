# How do I generate a fake email address using Laravel Faker?
// plain

Using Laravel Faker, you can generate a fake email address with the following code:

```
$faker = Faker\Factory::create();
$email = $faker->email;
echo $email;
```

## Output example


```
jasonmiller@hotmail.com
```

The code above uses the `Faker\Factory::create()` method to create a new Faker instance. The `$faker->email` method then generates a fake email address. Finally, the `echo` statement prints the generated email address to the console.

The code consists of the following parts:

* `Faker\Factory::create()`: Creates a new Faker instance.
* `$faker->email`: Generates a fake email address.
* `echo $email`: Prints the generated email address to the console.

For more information, see the [Laravel Faker documentation](https://github.com/fzaninotto/Faker#fakerprovideremail).

onelinerhub: [How do I generate a fake email address using Laravel Faker?](https://onelinerhub.com/php-faker/how-do-i-generate-a-fake-email-address-using-laravel-faker)