# input

How do I add a label to an input field in ReactJS?
// plain

The easiest way to add a label to an input field in ReactJS is to include the `<label>` tag inside the `<input>` tag. For example:

```
<input type="text" id="name">
<label for="name">Enter your name</label>
```

This will create a label with the text "Enter your name" that is associated with the input field. The `for` attribute of the `<label>` tag should match the `id` attribute of the `<input>` tag.

Besides the `<label>` tag, you can also use the `aria-label` attribute of the `<input>` tag to add a label to the input field. For example:

```
<input type="text" aria-label="name">
```

This will create a label with the text "name" for the input field.

You can also use the `placeholder` attribute of the `<input>` tag to add a label to the input field. For example:

```
<input type="text" placeholder="Enter your name">
```

This will create a label with the text "Enter your name" inside the input field.

## Code explanation

- `<label>` tag: used to add a label to an input field
- `for` attribute: used to match the `<label>` tag with the `<input>` tag
- `aria-label` attribute: used to add a label to the `<input>` tag
- `placeholder` attribute: used to add a label inside the `<input>` tag

## Helpful links
- https://reactjs.org/docs/forms.html
- https://developer.mozilla.org/en-US/docs/Web/HTML/Element/label

onelinerhub: [input

How do I add a label to an input field in ReactJS?](https://onelinerhub.com/reactjs/input--how-do-i-add-a-label-to-an-input-field-in-reactjs)