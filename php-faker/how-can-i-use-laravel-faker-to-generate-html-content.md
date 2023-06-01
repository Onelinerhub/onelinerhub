# How can I use Laravel Faker to generate HTML content?
// plain

Laravel Faker can be used to generate HTML content by using the raw() method to generate an HTML string. This method can be used to generate HTML elements such as a `<p>` tag with a random string. The example below shows how to use the raw() method to generate a `<p>` element with a random string.

```
$faker = Faker\Factory::create();

echo $faker->raw("<p>{{randomString}}</p>");
```

## Output example

```
<p>VmE2OuVzU1</p>
```

The code above consists of the following parts:
1. `$faker = Faker\Factory::create();` - This creates a new Faker instance.
2. `echo $faker->raw("<p>{{randomString}}</p>");` - This uses the raw() method to generate an HTML string with a random string.

## Helpful links
- [Laravel Faker Documentation](https://github.com/fzaninotto/Faker#formatters)
- [Faker Raw Method Documentation](https://github.com/fzaninotto/Faker#raw-formatters)

onelinerhub: [How can I use Laravel Faker to generate HTML content?](https://onelinerhub.com/php-faker/how-can-i-use-laravel-faker-to-generate-html-content)