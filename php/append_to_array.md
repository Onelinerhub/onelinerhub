# Append to an array

### Note: if appending a single element, the short form is preferable as it eliminates the overhead of calling the function.

```php
// Long
array_push($myarray, [1, 2, 'hatstand']);
// Long associative
array_push($myarray, ['three' => 'hatstand']);
// Short
$myarray[] = [1, 2, 'hatstand'];
// Short associative
$myarray['three'] = 'hatstand';
```

- ``array_push(`` - call the `array_push` function
- ``$myarray,`` - the array to push to
- ``[1, 2, 'hatstand']`` - the items to append
- ``$myarray[] =`` - open the array to append in shorthand
- ``['three' =>`` - the key to append
- ``'hatstand'`` - the value to append
- ``$myarray['three'] =`` - open the array to append with the key `three`
