# How can I use jQuery to yield a result?
// plain

jQuery is a JavaScript library that allows you to manipulate HTML elements. You can use jQuery to yield a result by selecting an element, performing some type of action on it, and then getting a result from it.

For example, you could use jQuery to get the text content of a `<p>` element:

```javascript
// Select the <p> element
let paragraph = $('p');

// Get the text content
let textContent = paragraph.text();

// Output the text content
console.log(textContent);
```

## Output example
 `This is the text content of the paragraph.`

## Code explanation


1. `let paragraph = $('p');` - This line selects the `<p>` element.
2. `let textContent = paragraph.text();` - This line gets the text content of the `<p>` element.
3. `console.log(textContent);` - This line outputs the text content of the `<p>` element.

For more information on jQuery, see the [jQuery Documentation](https://api.jquery.com/).

onelinerhub: [How can I use jQuery to yield a result?](https://onelinerhub.com/jquery/how-can-i-use-jquery-to-yield-a-result)