# Get static methods list of a class

```php
$methods = (new ReflectionClass('class1'))->getMethods(ReflectionMethod::IS_STATIC);
```

- $methods - will contain array of static methods
- 'class1' - name of static class to get methods of
- new ReflectionClass - create reflection of specified class
- getMethods( - will return methods of specified type
- ReflectionMethod::IS_STATIC - get static methods only
