# How can I use jQuery to select an element's siblings?
// plain

jQuery provides a method to select siblings of an element, called `.siblings()`. This method returns all sibling elements of the selected element.

## Example code

```
$("#myDiv").siblings();
```
## Output example

```
[<div id="sibling1"></div>, <div id="sibling2"></div>]
```

## Code explanation

- `$("#myDiv")`: This is a jQuery selector that selects the element with the id of "myDiv".
- `.siblings()`: This is a jQuery method that selects all sibling elements of the selected element.

## Helpful links
- [jQuery Siblings](https://api.jquery.com/siblings/)

onelinerhub: [How can I use jQuery to select an element's siblings?](https://onelinerhub.com/jquery/how-can-i-use-jquery-to-select-an-element-s-siblings)