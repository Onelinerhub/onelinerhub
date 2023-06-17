# How do I remove an element using jQuery?
// plain

To remove an element using jQuery, you can use the `remove()` method. This method removes the selected elements, including all text and child nodes.

For example:

```
<div class="example">
  <p>This is an example element.</p>
</div>

<script>
  $(".example").remove();
</script>
```

This will remove the `<div>` element with the class `example`, including all of its content.

The `remove()` method can also be used in combination with other jQuery methods, such as `find()` and `children()`, to remove specific elements.

For example:

```
<div class="example">
  <p>This is an example element.</p>
  <p>This is another example element.</p>
</div>

<script>
  $(".example").find("p").eq(1).remove();
</script>
```

This code will remove the second `<p>` element, leaving the first `<p>` element intact.

The `remove()` method can also be used to remove elements from the DOM and store them in a variable for later use.

For example:

```
<div class="example">
  <p>This is an example element.</p>
</div>

<script>
  var removedElement = $(".example").remove();
</script>
```

This code will remove the `<div>` element with the class `example`, including all of its content, and store it in the variable `removedElement`.

## Code explanation


- `$(".example")`: This is a jQuery selector that selects the element with the class `example`.
- `remove()`: This is the jQuery method that removes the selected elements, including all text and child nodes.
- `find()`: This is the jQuery method that searches the descendants of the selected element.
- `children()`: This is the jQuery method that searches the children of the selected element.
- `eq(1)`: This is the jQuery method that selects the element at the specified index.

#### List of ## Helpful links

- [jQuery - remove()](https://api.jquery.com/remove/)
- [jQuery - find()](https://api.jquery.com/find/)
- [jQuery - children()](https://api.jquery.com/children/)
- [jQuery - eq()](https://api.jquery.com/eq/)

onelinerhub: [How do I remove an element using jQuery?](https://onelinerhub.com/jquery/how-do-i-remove-an-element-using-jquery)