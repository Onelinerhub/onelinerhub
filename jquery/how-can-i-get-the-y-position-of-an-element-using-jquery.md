# How can I get the y position of an element using jQuery?
// plain

The y position of an element can be retrieved using the `.offset()` method in jQuery. The `.offset()` method allows you to retrieve the current coordinates of the first element in the set of matched elements, in relation to the document.

## Example

```
let yPosition = $("#element").offset().top;
console.log(yPosition);
```
## Output example
 `100`

The code above will retrieve the y position of the element with the id of `#element` and store it in the `yPosition` variable.

Parts of the code:
- `$("#element")`: This will select the element with the id of `#element`
- `.offset()`: This will retrieve the current coordinates of the element
- `.top`: This will retrieve the y position of the element
- `console.log(yPosition)`: This will log the y position of the element to the console

## Helpful links
- [jQuery .offset() Documentation](https://api.jquery.com/offset/)

onelinerhub: [How can I get the y position of an element using jQuery?](https://onelinerhub.com/jquery/how-can-i-get-the-y-position-of-an-element-using-jquery)