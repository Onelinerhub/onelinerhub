# How do I use PHP Faker to generate XML data?
// plain

Using PHP Faker to generate XML data is easy. First, you need to include the Faker library.

```php
require_once 'vendor/autoload.php';
```

Then, create a Faker instance:

```php
$faker = Faker\Factory::create();
```

To generate the XML data, use the `toXml()` method:

```php
$xml = $faker->toXml();
```

This will return a string of XML data. For example:

```
<?xml version="1.0" encoding="UTF-8"?>
<root>
  <person>
    <name>Samantha</name>
    <address>
      <streetAddress>764</streetAddress>
      <city>New Jazmyne</city>
      <postcode>45288-4257</postcode>
    </address>
  </person>
</root>
```

The `toXml()` method also takes an optional parameter which is an array of attributes. For example:

```php
$xml = $faker->toXml(['version' => '1.1']);
```

This will generate XML data with the version attribute set to 1.1.

## Helpful links

- [PHP Faker Documentation](https://github.com/fzaninotto/Faker#fakerprovidertoxml)

onelinerhub: [How do I use PHP Faker to generate XML data?](https://onelinerhub.com/php-faker/how-do-i-use-php-faker-to-generate-xml-data)