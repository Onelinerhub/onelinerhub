# How to mock a query builder with PHPUnit?
// plain

Mocking a query builder with PHPUnit can be done using the `getMockBuilder` method. This method allows you to create a mock object of a given class.

```php
$mockQueryBuilder = $this->getMockBuilder('QueryBuilder')
    ->setMethods(['select', 'from', 'where', 'orderBy', 'limit'])
    ->getMock();
```

The code above creates a mock object of the `QueryBuilder` class with the methods `select`, `from`, `where`, `orderBy` and `limit`.

## Code explanation


- `getMockBuilder`: This method creates a mock object of a given class.
- `setMethods`: This method sets the methods that should be mocked.
- `getMock`: This method returns the mock object.

## Helpful links

- [PHPUnit Documentation - Mock Objects](https://phpunit.readthedocs.io/en/9.2/test-doubles.html#test-doubles-mock-objects)

onelinerhub: [How to mock a query builder with PHPUnit?](https://onelinerhub.com/phpunit/how-to-mock-a-query-builder-with-phpunit)