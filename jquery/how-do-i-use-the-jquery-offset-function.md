# How do I use the jQuery offset function?
// plain

The jQuery offset() function is used to retrieve the current coordinates of an element relative to the document. It can be used to determine the position of an element on the page.

## Example

```
var position = $("#element").offset();
```

## Output example

```
Object {top: 8, left: 8}
```

The output returns an object with two properties, top and left. These properties represent the distance from the top and left edges of the document, respectively.

The following is a list of parts of the code and their explanations:

- `$("#element")`: This is the jQuery selector used to select the element with the ID of "element".
- `offset()`: This is the jQuery offset() function, which is used to retrieve the current coordinates of the selected element.
- `top`: This is a property of the object returned by the offset() function, which represents the distance from the top edge of the document.
- `left`: This is a property of the object returned by the offset() function, which represents the distance from the left edge of the document.

## Helpful links
- [jQuery offset() Documentation](https://api.jquery.com/offset/)

onelinerhub: [How do I use the jQuery offset function?](https://onelinerhub.com/jquery/how-do-i-use-the-jquery-offset-function)