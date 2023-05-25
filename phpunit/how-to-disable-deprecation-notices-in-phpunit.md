# How to disable deprecation notices in PHPUnit?
// plain

To disable deprecation notices in PHPUnit, you can use the `@group` annotation. This annotation allows you to group tests together and apply settings to the entire group. To disable deprecation notices, you can add the `@group disableDeprecation` annotation to the top of your test class.

```
<?php

/**
 * @group disableDeprecation
 */
class MyTest extends \PHPUnit_Framework_TestCase
{
    // ...
}
```

This will disable all deprecation notices for all tests in the `MyTest` class.

## Code explanation


1. `@group` annotation - This annotation allows you to group tests together and apply settings to the entire group.
2. `@group disableDeprecation` annotation - To disable deprecation notices, you can add this annotation to the top of your test class.
3. `MyTest` class - This will disable all deprecation notices for all tests in the `MyTest` class.

## Helpful links

- [PHPUnit Documentation - Group Annotations](https://phpunit.readthedocs.io/en/latest/annotations.html#group)

onelinerhub: [How to disable deprecation notices in PHPUnit?](https://onelinerhub.com/phpunit/how-to-disable-deprecation-notices-in-phpunit)