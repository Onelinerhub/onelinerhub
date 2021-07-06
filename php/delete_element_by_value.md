# Delete an element from array by value

```php
if (( $k = array_search($val, $arr)) !== false ) unset($arr[$k]);
```

- array_search( - will find key of an element with `$val` value
- $k - will have key of searched element (if any was found)
- $val - value to search in array
- $arr - array to search value in
- unset($arr\[$k\]) - remove found element from array

group: delete_from_array
