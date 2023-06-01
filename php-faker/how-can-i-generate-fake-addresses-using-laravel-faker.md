# How can I generate fake addresses using Laravel Faker?
// plain

Using the [Laravel Faker](https://github.com/fzaninotto/Faker) library you can generate fake addresses with the following code:

```
$faker = Faker::create();

echo $faker->streetAddress;
```

This will output a fake street address, such as:

```
906 Watsica Summit
```

You can also generate a full address with the following code:

```
echo $faker->address;
```

This will output a full address, such as:

```
906 Watsica Summit, South Lillie, Vermont 84737
```

You can also customize the address with the following code:

```
echo $faker->streetAddress . ', ' . $faker->city . ', ' . $faker->state . ' ' . $faker->postcode;
```

This will output a full address, such as:

```
906 Watsica Summit, South Lillie, Vermont 84737
```

You can also generate a random country with the following code:

```
echo $faker->country;
```

This will output a random country, such as:

```
Czech Republic
```

For more information, refer to the [Laravel Faker documentation](https://github.com/fzaninotto/Faker).

onelinerhub: [How can I generate fake addresses using Laravel Faker?](https://onelinerhub.com/php-faker/how-can-i-generate-fake-addresses-using-laravel-faker)