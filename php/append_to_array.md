# How to append an element to array

```php
$myarray[] = 'hatstand';
```

- `$myarray` - the array to push element to
- `[]` - array append operator
- `hatstand` - element to append to array

group: append

## Example: 
```php
<?php

$myarray = [1,2];
$myarray[] = 'new_val';

print_r($myarray);
```
```
Array
(
    [0] => 1
    [1] => 2
    [2] => new_val
)

```

