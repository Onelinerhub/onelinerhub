# Convert Persian English Number To Persian Number
```php
function fa_number($number)
{
   if(!is_numeric($number) || empty($number))
   return '۰';
   $en = array("0","1","2","3","4","5","6","7","8","9");
   $fa = array("۰","۱","۲","۳","۴","۵","۶","۷","۸","۹");
   return str_replace($en, $fa, $number);
}
```