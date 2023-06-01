# How can I use PHP Elastica to generate a hash?
// plain

PHP Elastica is a library that can be used to create a hash. A hash is a data structure that stores values in key-value pairs.

To use PHP Elastica to generate a hash, you need to include the library in your code.

```php
require_once 'vendor/autoload.php';
```

Then, you can use the `Elastica\Hash` class to create a hash object.

```php
$hash = new Elastica\Hash();
```

You can use the `set()` and `get()` methods to add and retrieve values from the hash.

```php
$hash->set('foo', 'bar');
$value = $hash->get('foo');
// $value is now 'bar'
```

You can also use the `has()` method to check if a key exists in the hash.

```php
$exists = $hash->has('foo');
// $exists is now true
```

You can find more information about PHP Elastica and hashes in the [documentation](https://www.elastica.io/docs/).

## Code explanation
**

1. `require_once 'vendor/autoload.php'` - This line includes the PHP Elastica library in the code.
2. `$hash = new Elastica\Hash()` - This line creates a new Elastica\Hash object.
3. `$hash->set('foo', 'bar')` - This line adds a key-value pair to the hash.
4. `$value = $hash->get('foo')` - This line retrieves the value associated with the 'foo' key from the hash.
5. `$exists = $hash->has('foo')` - This line checks if the 'foo' key exists in the hash.

**Output of example code:**

```
$value is now 'bar'
$exists is now true
```

onelinerhub: [How can I use PHP Elastica to generate a hash?](https://onelinerhub.com/php-elastica/how-can-i-use-php-elastica-to-generate-a-hash)