# How do I use jQuery to get an element's ID?
// plain

To get an element's ID using jQuery, you can use the `attr()` function.

```
// Get the ID of the element with id="example"
var elementID = $("#example").attr('id');
console.log(elementID);
```

## Output example
 `example`

The code above consists of the following parts:
- `$("#example")`: This is a jQuery selector that selects the element with the ID of `example`.
- `attr('id')`: This is a jQuery function that returns the value of the `id` attribute of the selected element.
- `var elementID =`: This creates a variable called `elementID` to store the ID of the element.
- `console.log(elementID)`: This prints the value of the `elementID` variable to the console.

## Helpful links
- https://api.jquery.com/attr/
- https://www.w3schools.com/js/js_variables.asp

onelinerhub: [How do I use jQuery to get an element's ID?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-get-an-element-s-id)