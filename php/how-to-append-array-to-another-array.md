# How to append array to another array

```php
$arr1 = [1,2];
$arr2 = [3,4];
$res = array_merge($arr1, $arr2);
```

- `$arr1, $arr2` - arrays to append to each other
- `array_merge` - will append given arrays to each other
- `$res` - will store resulting array

group: append

## Example: 
```php
<?php

$arr1 = [1,2];
$arr2 = [3,4];
$res = array_merge($arr1, $arr2);

print_r($res);
```
```
Array
(
    [0] => 1
    [1] => 2
    [2] => 3
    [3] => 4
)

```

