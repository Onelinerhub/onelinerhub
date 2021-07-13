# Insert element to an array on a certain position

```php
array_splice($arr, 2, 0, $insert);
```

- array_splice - replaces or inserts parts of array
- $arr - array to insert new value to
- 2 - position to insert new value at (starts from `0`, so we're inserting 3rd element)
- 0 - don't delete any elements from original array
- $insert - value to insert

## Example
```php
$arr = [1, 2, 3];
array_splice($arr, 2, 0, 'a');
print_r($arr);
```
```
Array
(
    [0] => 1
    [1] => 2
    [2] => a
    [3] => 3
)
```
