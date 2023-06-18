# input

How can I use a hidden input in ReactJS?
// plain

A hidden input in ReactJS can be used to store information that should not be displayed to the user, such as session tokens or other sensitive data. To create a hidden input, you will need to use the `<input type="hidden">` tag. This tag will create an input element that is not visible on the page, but can still be used in form submissions.

For example, the following code will create a hidden input with the value of `12345`:

```js
<input type="hidden" value="12345" />
```

The `value` attribute of the input tag is used to set the value of the hidden input. This value can then be accessed in the form submission and used to store the data.

It is important to note that a hidden input should only be used for data that should not be visible to the user. It should not be used to store confidential information, such as passwords or credit card numbers.

## Code explanation


- `<input type="hidden">`: This tag will create an input element that is not visible on the page, but can still be used in form submissions.
- `value` attribute: This attribute is used to set the value of the hidden input.

Here is a list of ## Helpful links

- [React Input](https://reactjs.org/docs/forms.html#controlled-components)
- [MDN Input Element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input)

onelinerhub: [input

How can I use a hidden input in ReactJS?](https://onelinerhub.com/reactjs/input--how-can-i-use-a-hidden-input-in-reactjs)