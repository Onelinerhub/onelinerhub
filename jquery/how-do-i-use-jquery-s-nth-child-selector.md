# How do I use jQuery's nth-child selector?
// plain

jQuery's nth-child selector is used to select elements based on their position within a group of siblings. It is an efficient way to select elements without having to use classes or IDs.

## Example

```
$("ul li:nth-child(2)").css("background-color", "red");
```
This example will select the second <li> element inside of an unordered list and apply a background color of red.

## Code explanation

* $("ul li:nth-child(2)") - This is the jQuery selector which will select the second <li> element inside of an unordered list.
* .css("background-color", "red") - This is the jQuery method which will apply a background color of red to the selected element.

## Helpful links
* [jQuery nth-child Selector Documentation](http://api.jquery.com/nth-child-selector/)
* [jQuery css() Method Documentation](http://api.jquery.com/css/)

onelinerhub: [How do I use jQuery's nth-child selector?](https://onelinerhub.com/jquery/how-do-i-use-jquery-s-nth-child-selector)