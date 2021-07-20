# Sort multidimensional array

```php
usort($arr, function($a, $b) { return $a['val'] <=> $b['val']; });
```

- usort( - this function sorts specified array by custom fiven function
- $arr - array to sort (this variable will contain sorted array after sorting)
- function($a, $b) - custom function will get `$a` and `$b`, which are two elements from array to compare
- $a\['val'\] <=> $b\['val'\] - compare keys of array elements

group: sort_objects
