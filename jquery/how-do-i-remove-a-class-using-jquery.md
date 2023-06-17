# How do I remove a class using jQuery?
// plain

Removing a class from an element using jQuery is simple. To do so, you can use the `removeClass()` method. This method takes one argument, the class that you want to remove. Here is an example:

```
$("p").removeClass("intro");
```

This code will remove the class "intro" from all `<p>` elements on the page.

The `removeClass()` method is part of the jQuery API and is used to manipulate the class attribute of an element. It takes one argument, the class name that you want to remove. If you want to remove multiple classes, you can pass a space-separated list of classes as the argument.

## Code explanation


* `$("p")` - This is a jQuery selector that selects all `<p>` elements on the page.

* `removeClass()` - This is the method used to remove a class from an element.

* `"intro"` - This is the class name that is being removed from the `<p>` elements.

## Helpful links

* [jQuery removeClass()](https://api.jquery.com/removeClass/) - jQuery API documentation on the `removeClass()` method.

onelinerhub: [How do I remove a class using jQuery?](https://onelinerhub.com/jquery/how-do-i-remove-a-class-using-jquery)