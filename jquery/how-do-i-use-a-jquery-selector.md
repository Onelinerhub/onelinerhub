# How do I use a jQuery selector?
// plain

jQuery selectors are used to select elements on a page based on their HTML attributes, such as id, class, type, and more.

The syntax for using jQuery selectors is as follows:

```javascript
$(selector).action()
```

where `selector` is the element or group of elements you want to select, and `action` is the action you want to take on the elements.

For example, to select all `<p>` elements on a page and make them red, you could use the following code:

```javascript
$("p").css("color", "red");
```

The code above will select all `<p>` elements on the page and change their color to red.

Here is a list of the most commonly used jQuery selectors:

* `$("*")` - selects all elements on the page
* `$("#id")` - selects an element by its id
* `$(".class")` - selects elements by their class
* `$("element")` - selects elements by their HTML element type

You can also use multiple selectors to select elements in combination, for example:

```javascript
$("p.intro").css("color", "blue");
```

The code above will select all `<p>` elements with the class `intro` and make them blue.

For more information on jQuery selectors, please visit the following links:

* [jQuery Selectors](https://api.jquery.com/category/selectors/)
* [jQuery Selectors Cheat Sheet](https://oscarotero.com/jquery/)

onelinerhub: [How do I use a jQuery selector?](https://onelinerhub.com/jquery/how-do-i-use-a-jquery-selector)