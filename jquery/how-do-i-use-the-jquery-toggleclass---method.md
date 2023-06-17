# How do I use the jQuery toggleClass() method?
// plain

The jQuery `toggleClass()` method is used to toggle between adding and removing one or more classes from the selected elements.

#### Example

```javascript
$("button").click(function(){
    $("div").toggleClass("active");
});
```

This example will toggle the `active` class on the `div` element when the `button` is clicked.

#### Explanation

The `toggleClass()` method takes two parameters:

1. `className`: A string representing one or more class names to be toggled.
2. `switch`: A Boolean value that determines whether the class should be added or removed.

If the `switch` parameter is omitted, the class will be toggled on or off depending on the current state of the element.

#### Relevant Links

- [jQuery toggleClass() Documentation](https://api.jquery.com/toggleclass/)

onelinerhub: [How do I use the jQuery toggleClass() method?](https://onelinerhub.com/jquery/how-do-i-use-the-jquery-toggleclass---method)