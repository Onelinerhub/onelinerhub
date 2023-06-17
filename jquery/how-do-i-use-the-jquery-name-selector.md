# How do I use the jQuery name selector?
// plain

The jQuery name selector allows you to select elements on the page by their name attribute. To use the selector, you need to pass the name attribute value as a string argument to the `$()` function. For example, the following code will select all elements with the name attribute "name":

```
$("[name='name']")
```

The output of this code is a jQuery object containing all elements with the name attribute "name". You can then use jQuery methods on this object to manipulate the elements.

The following code will change the background color of all elements with the name attribute "name":

```
$("[name='name']").css("background-color", "red");
```

The code consists of two parts:

1. `$("[name='name']")` - This part selects all elements with the name attribute "name".
2. `.css("background-color", "red")` - This part changes the background color of all elements to red.

For more information about the jQuery name selector, please refer to the following links:

- [jQuery Selectors](https://api.jquery.com/category/selectors/)
- [Attribute Equals Selector](https://api.jquery.com/attribute-equals-selector/)

onelinerhub: [How do I use the jQuery name selector?](https://onelinerhub.com/jquery/how-do-i-use-the-jquery-name-selector)