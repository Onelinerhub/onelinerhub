# Format number with leading zeros

```php
str_pad($num, 10, '0', STR_PAD_LEFT);
```

- str_pad - will add specified amount of characters to the string
- $num - number to add zeros to
- 10 - total length of resulting number with zeros
- '0' - symbol to add to number (zero in our case)
- STR_PAD_LEFT - add zeros to the left side of the number

group: str_pad
