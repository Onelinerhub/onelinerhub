# How can I use jQuery to access data attributes?
// plain

jQuery provides a simple way to access data attributes using the `.data()` method. This method takes the name of the data attribute as its argument and returns the value of the data attribute. The following example code block demonstrates how to access a data attribute called `data-example`:

```
var example = $('#example').data('example');
console.log(example); // Output: 'This is an example'
```

The code above is composed of the following parts:

1. `var example =` - This declares a variable called `example` which will store the value of the data attribute.
2. `$('#example')` - This selects the element with the id of `example` and stores it in a jQuery object.
3. `.data('example')` - This accesses the data attribute called `example` from the jQuery object.
4. `console.log(example)` - This prints the value of the data attribute to the console.

You can also use the `.attr()` method to access data attributes. This method takes the name of the attribute as its argument, and returns the value of the attribute. The following example demonstrates how to access the data attribute using the `.attr()` method:

```
var example = $('#example').attr('data-example');
console.log(example); // Output: 'This is an example'
```

For more information, please see the following links:

- [jQuery .data()](https://api.jquery.com/data/)
- [jQuery .attr()](https://api.jquery.com/attr/)

onelinerhub: [How can I use jQuery to access data attributes?](https://onelinerhub.com/jquery/how-can-i-use-jquery-to-access-data-attributes)