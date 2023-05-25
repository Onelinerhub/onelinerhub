# How to load fixtures with PHPUnit?
// plain

PHPUnit provides a way to load fixtures with the `DataSet` class. Fixtures are data used to test the application.

## Example code

```php
<?php
use PHPUnit\Framework\TestCase;

class MyTest extends TestCase
{
    public function testFixtures()
    {
        // Load the fixtures
        $fixtureData = $this->createMySQLXMLDataSet(__DIR__ . '/fixtures.xml');
        // Use the fixtures
        $this->assertEquals($fixtureData->getTable('users')->getRow(0), array('id' => 1, 'name' => 'John'));
    }
}
```

The code above loads the fixtures from the `fixtures.xml` file and then uses the data to assert that the first row of the `users` table has the `id` of `1` and the `name` of `John`.

The `DataSet` class provides several methods to load fixtures from different formats, such as XML, CSV, JSON, YAML, and PHP.

- `createMySQLXMLDataSet`: Loads fixtures from an XML file in the MySQL XML format.
- `createCsvDataSet`: Loads fixtures from a CSV file.
- `createJsonDataSet`: Loads fixtures from a JSON file.
- `createYamlDataSet`: Loads fixtures from a YAML file.
- `createArrayDataSet`: Loads fixtures from a PHP array.

## Helpful links
- [PHPUnit Documentation - Data Sets](https://phpunit.readthedocs.io/en/9.2/fixtures.html#data-sets)

onelinerhub: [How to load fixtures with PHPUnit?](https://onelinerhub.com/phpunit/how-to-load-fixtures-with-phpunit)