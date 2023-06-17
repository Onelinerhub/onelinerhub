# How do I convert a jQuery script to vanilla JavaScript?
// plain

Converting a jQuery script to vanilla JavaScript can be done by replacing jQuery methods with equivalent vanilla JavaScript methods. For example, the following jQuery code:
```
$('#myElement').addClass('active');
```
can be converted to vanilla JavaScript by using the `classList.add()` method:
```
document.getElementById('myElement').classList.add('active');
```

## Code explanation


- `$('#myElement')` - This uses jQuery's `$()` function to select an element with the ID of `myElement`.
- `.addClass('active')` - This uses jQuery's `addClass()` method to add the class `active` to the element.
- `document.getElementById('myElement')` - This uses the vanilla JavaScript `getElementById()` method to select an element with the ID of `myElement`.
- `.classList.add('active')` - This uses the vanilla JavaScript `classList.add()` method to add the class `active` to the element.

For more information, see the following links:

- [jQuery - Selectors](https://api.jquery.com/category/selectors/)
- [Element.classList](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList)

onelinerhub: [How do I convert a jQuery script to vanilla JavaScript?](https://onelinerhub.com/jquery/how-do-i-convert-a-jquery-script-to-vanilla-javascript)