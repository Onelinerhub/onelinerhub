# How can I use jQuery to get the inner text of an element?
// plain

Using jQuery, you can get the inner text of an element with the `.text()` method. This method takes no parameters and returns the text content of the selected element.

For example, given the following HTML:
```
<div id="example">
  Hello World
</div>
```

You can use the following jQuery code to get the inner text of the element:
```javascript
var text = $("#example").text();
console.log(text);
```

This will output the following to the console:
```
Hello World
```

The `.text()` method can be broken down into the following parts:
1. `$("#example")` - This part of the method selects the element with the id of `example` using jQuery's selector syntax.
2. `.text()` - This part of the method calls the `text()` method on the selected element, returning the inner text of the element.

For more information on the `.text()` method, see [this page](https://api.jquery.com/text/).

onelinerhub: [How can I use jQuery to get the inner text of an element?](https://onelinerhub.com/jquery/how-can-i-use-jquery-to-get-the-inner-text-of-an-element)