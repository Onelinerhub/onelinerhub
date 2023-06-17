# How can I format a number using jQuery?
// plain

jQuery provides a function called `.number()` that can be used to format numbers. The syntax for this function is `.number( number [, decimals ] [, decPoint ] [, thousandsSep ] )` where `number` is the number to be formatted, `decimals` is the number of decimal places, `decPoint` is the character to use as the decimal point, and `thousandsSep` is the character to use as the thousands separator.

For example, the following code:
```
var number = 1234.567;
$('#result').text($.number(number, 2, '.', ','));
```

will output `1,234.57` in the element with id `result`.

## Code explanation

- `number` - the number to be formatted
- `decimals` - the number of decimal places
- `decPoint` - the character to use as the decimal point
- `thousandsSep` - the character to use as the thousands separator

## Helpful links
- [jQuery.number() | jQuery API Documentation](https://api.jquery.com/jQuery.number/)

onelinerhub: [How can I format a number using jQuery?](https://onelinerhub.com/jquery/how-can-i-format-a-number-using-jquery)