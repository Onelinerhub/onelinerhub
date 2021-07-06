# Delete an element from an array

```php
unset($arr[1]);
```

- $arr - array to delete element from
- \[1\] - element index to delete (2nd element in our case)

## Example
```php
$arr = [1, 2, 3];
unset($arr[1]);
print_r($arr);
```
```bash
Array
(
    [0] => 1
    [2] => 3
)
```

group: delete_from_array
