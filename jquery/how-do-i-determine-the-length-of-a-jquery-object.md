# How do I determine the length of a jQuery object?
// plain

The length of a jQuery object can be determined by using the `length` property. The `length` property returns the number of elements in the jQuery object.

For example:
```
var jqObj = $("div");
console.log(jqObj.length);
```
The output of this code will be the number of `<div>` elements on the page.

## Code explanation

* `var jqObj = $("div");` - This creates a jQuery object containing all `<div>` elements on the page.
* `jqObj.length` - This returns the number of elements in the jQuery object.
* `console.log(jqObj.length);` - This prints the number of elements in the jQuery object to the console.

## Helpful links
* [jQuery.length](https://api.jquery.com/length/) - Documentation for the `length` property.

onelinerhub: [How do I determine the length of a jQuery object?](https://onelinerhub.com/jquery/how-do-i-determine-the-length-of-a-jquery-object)