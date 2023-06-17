# How do I use jQuery to append an element after another element?
// plain

To use jQuery to append an element after another element, the following steps can be taken:

1. Create a jQuery object for the element that you want to append after, for example:
```
var element = $('#elementId');
```
2. Create a jQuery object for the element that you want to append, for example:
```
var appendElement = $('<div>Append Element</div>');
```
3. Use the `after()` method to append the element, for example:
```
element.after(appendElement);
```

This will append the `appendElement` element after the `element` element.

## Helpful links
- [jQuery after() Method](https://www.w3schools.com/jquery/jquery_dom_add.asp)
- [jQuery append() Method](https://www.w3schools.com/jquery/jquery_dom_add.asp)

onelinerhub: [How do I use jQuery to append an element after another element?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-append-an-element-after-another-element)