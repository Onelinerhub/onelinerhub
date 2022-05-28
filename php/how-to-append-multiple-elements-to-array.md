# How to append multiple elements to array

```php
array_push($myarray, 3, 4, 5);
```

- `$myarray` - the array to push element to
- `3, 4, 5` - list of values to append (can be any number of values)
- `array_push` - will append specified values (2... arguments) to given array (first argument)

group: append

## Example: 
```php
<?php

$myarray = [1,2];
array_push($myarray, 3, 4, 5);

print_r($myarray);
```
```
Array
(
    [0] => 1
    [1] => 2
    [2] => 3
    [3] => 4
    [4] => 5
)

```

