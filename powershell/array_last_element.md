# How to retrieve last element of array

### This code first retrieves the keys of the `$arr` array using the `keys` property, then uses the `select` cmdlet with the `-last 1` parameter to retrieve the last key of the array. Finally, it retrieves the value at that key from the `$arr` array and assigns it to the `$last` variable.


```bash
$last = $arr[$arr.keys | select -last 1]
```
