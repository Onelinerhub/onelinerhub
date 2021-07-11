# Have exactly 2 decimal places for the number

```php
number_format( floatval($num), 2, '.', ',' );
```

- number_format - formats specified number
- floatval - convert number to float so it always has decimals
- $num - number to format
- 2 - number of decimals to have
- '.' - decimals separator
- ',' - thousands separator
