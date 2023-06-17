# How can I use jQuery to get data attributes?
// plain

jQuery provides a convenient way to access data attributes on an HTML element using the `data()` method.

For example, to get the value of a data attribute called `data-example` on an element with the ID `example`, you can use the following code:

```
var exampleValue = $('#example').data('example');
console.log(exampleValue);
```

The output of the above code will be the value of the `data-example` attribute.

The code can be broken down as follows:

1. `$('#example')` - this selects the element with the ID `example` using jQuery.
2. `data('example')` - this retrieves the value of the `data-example` attribute from the element.

For more information, see the following resources:

- [jQuery Data() Method](https://www.w3schools.com/jquery/jquery_data.asp)
- [jQuery Selectors](https://www.w3schools.com/jquery/jquery_selectors.asp)

onelinerhub: [How can I use jQuery to get data attributes?](https://onelinerhub.com/jquery/how-can-i-use-jquery-to-get-data-attributes)