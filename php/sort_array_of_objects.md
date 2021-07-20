# Sort array of objects by specific property

```php
usort($objs, function($a, $b) { return $a->val <=> $b->val; });
```

- usort( - this function sorts specified array by custom fiven function
- $objs - array of objects to sort (this variable will contain sorted array after sorting)
- function($a, $b) - custom function will get `$a` and `$b`, which are two objects from array to compare
- $a->val <=> $b->val - compare properties of objects

group: sort_objects
