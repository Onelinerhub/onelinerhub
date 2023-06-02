# How do I generate a valid VAT number using Laravel Faker?
// plain

Generating valid VAT numbers using Laravel Faker is easy. The Faker package provides a `vat()` method that returns a valid VAT number. Here is an example of how to generate a valid VAT number using Laravel Faker:

```
$faker = Faker\Factory::create();
$vatNumber = $faker->vat();
echo $vatNumber;
```

## Output example

```
DE129735358
```

The `vat()` method takes two optional parameters:

- `countryCode`: A string representing the ISO 3166-1 alpha-2 country code of the VAT number. Default value is `null`.
- `vatNumber`: A string representing the VAT number. Default value is `null`.

Here is an example of how to generate a valid VAT number with a specific country code using Laravel Faker:

```
$faker = Faker\Factory::create();
$vatNumber = $faker->vat('DE');
echo $vatNumber;
```

## Output example

```
DE129735358
```

## Helpful links
- [Laravel Faker Documentation](https://github.com/fzaninotto/Faker#fakerprovidevat)
- [ISO 3166-1 alpha-2 Country Codes](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)

onelinerhub: [How do I generate a valid VAT number using Laravel Faker?](https://onelinerhub.com/php-faker/how-do-i-generate-a-valid-vat-number-using-laravel-faker)