# How do I use the jQuery not selector?
// plain

The jQuery not selector is used to select all elements that do not match a given selector. It is used to filter out certain elements that are not of interest.

## Example

```
$('div:not(.myClass)').hide();
```
This code will hide all div elements that do not have the class "myClass".

The code consists of three parts:
1. The jQuery selector, `$('div:not(.myClass)')` which selects all div elements that do not have the class "myClass".
2. The jQuery action, `hide()` which hides the selected elements.
3. The semicolon `;` which marks the end of the statement.

For more information, see the [jQuery not selector documentation](https://api.jquery.com/not-selector/).

onelinerhub: [How do I use the jQuery not selector?](https://onelinerhub.com/jquery/how-do-i-use-the-jquery-not-selector)