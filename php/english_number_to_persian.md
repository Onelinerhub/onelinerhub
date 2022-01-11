# Convert standard numbers to Persian numbers

```php
function fa_number($number)
{
  if ( !is_numeric($number) || empty($number) ) return '۰';
  
  $en = array("0","1","2","3","4","5","6","7","8","9");
  $fa = array("۰","۱","۲","۳","۴","۵","۶","۷","۸","۹");
  
  return str_replace($en, $fa, $number);
}
```

- `fa_number` - function name to use later
- `$en` - list of standard numbers
- `$fa` - list of corresponding Persian numbers

## Example: 
```php
<?php

function fa_number($number)
{
  if(!is_numeric($number) || empty($number)) return '۰';
  
  $en = array("0","1","2","3","4","5","6","7","8","9");
  $fa = array("۰","۱","۲","۳","۴","۵","۶","۷","۸","۹");
  
  return str_replace($en, $fa, $number);
}

echo fa_number(12345);
```
```
۱۲۳۴۵
```

