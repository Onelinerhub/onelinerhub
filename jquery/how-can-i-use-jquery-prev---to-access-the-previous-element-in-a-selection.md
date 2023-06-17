# How can I use jQuery prev() to access the previous element in a selection?
// plain

The jQuery `prev()` method can be used to access the previous element in a selection. This method will traverse the DOM tree to find the previous sibling of the selected element.

## Example code

```
<div>
  <p>This is the first paragraph.</p>
  <p>This is the second paragraph.</p>
  <p>This is the third paragraph.</p>
</div>

<script>
  $( "p:last" ).prev().css( "background-color", "red" );
</script>
```

## Output example

```
<div>
  <p>This is the first paragraph.</p>
  <p style="background-color: red;">This is the second paragraph.</p>
  <p>This is the third paragraph.</p>
</div>
```

The code above will select the last `<p>` element in the selection, then use the `prev()` method to select the previous `<p>` element. The `css()` method is then used to set the background color of the element to red.

## Code explanation


1. `$( "p:last" )` - This will select the last `<p>` element in the selection.
2. `prev()` - This will traverse the DOM tree to find the previous sibling of the selected element.
3. `css( "background-color", "red" )` - This will set the background color of the element to red.

## Helpful links

- [jQuery prev() Method](https://www.w3schools.com/jquery/jquery_traversing_prev.asp)
- [jQuery css() Method](https://www.w3schools.com/jquery/jquery_css.asp)

onelinerhub: [How can I use jQuery prev() to access the previous element in a selection?](https://onelinerhub.com/jquery/how-can-i-use-jquery-prev---to-access-the-previous-element-in-a-selection)