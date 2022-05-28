# How to append an element to the beginning of array

```php
$myarray = [1,2];
array_unshift($myarray, 'hatstand');
```

- `$myarray` - the array to append new element to
- `array_unshift` - will append given value (`hatstand`) to the beginning of given array (`$myarr`), array will be updated
- `hatstand` - value to append to array

group: append

## Example: 
```php
<?php

$myarray = [1,2];
array_unshift($myarray, 'hatstand');

print_r($myarray);
```
```
Array
(
    [0] => hatstand
    [1] => 1
    [2] => 2
)

```

