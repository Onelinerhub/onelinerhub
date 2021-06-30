# Check if string contains specific substring

```php
if ( strpos($str, 'test') !== false ) { echo 'it is'; }
```

- strpos - this function will return position of found substring
- $str - string variable to search in
- 'test' - substring to search for
- !== false - use strict comparison, because of ```0 == false``` issue
- echo 'it is'; - execute this code when string contains needed substring


other_way: php 8 new function

```php
if ( str_contains($str, 'test') ) { echo 'it is'; }
```
- str_contains - new php 8 function that returns ```true``` if substring is found in a string
