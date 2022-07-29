# Find the position of a letter in the alphabet

```php
$alphabet = 'abcdefghijklmnopqrstuvwxyz';
$to_find = 'e';
echo strpos($alphabet, $to_find) + 1;
```

- ``$alphabet`` - the 'haystack', the string to be searched
- ``$to_find`` - the 'needle', the string to search for
- ``strpos(`` - finds the position of...
- ``+ 1`` - add to the index by one (to make up for indexing arrays from 0)

group: alphabet

## Example: 
```php
<?php

$alphabet = 'abcdefghijklmnopqrstuvwxyz';
$to_find = 'e';
echo strpos($alphabet, $to_find) + 1;
```
```
5
```

