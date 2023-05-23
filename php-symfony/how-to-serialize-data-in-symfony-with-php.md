# How to serialize data in Symfony with PHP?
// plain

Serializing data in Symfony with PHP can be done using the `serialize()` function. This function takes a single parameter, which is the value to be serialized. For example:

```php
$data = array('name' => 'John', 'age' => 25);
$serializedData = serialize($data);
```

The output of the above code will be a string representation of the array:

```
a:2:{s:4:"name";s:4:"John";s:3:"age";i:25;}
```

## Code explanation


- `serialize()`: This is the function used to serialize data.
- `$data`: This is the array that will be serialized.
- `$serializedData`: This is the variable that will contain the serialized data.

No relevant links.

onelinerhub: [How to serialize data in Symfony with PHP?](https://onelinerhub.com/php-symfony/how-to-serialize-data-in-symfony-with-php)