# How do I use jQuery to get an element by its ID?
// plain

Using jQuery to get an element by its ID is very simple. To do this, you can use the `$(#id)` selector. This will return a jQuery object containing all elements with the specified ID.

For example:

```
<div id="example">This is an example</div>

<script>
    var exampleElement = $('#example');
    console.log(exampleElement);
</script>
```

## Output example

```
[div#example]
```

The code above does the following:

1. Declares a `<div>` element with an ID of `example`.
2. Uses the `$('#example')` selector to get the element with an ID of `example`.
3. Stores the element in the `exampleElement` variable.
4. Logs the `exampleElement` variable to the console.

## Helpful links

- [jQuery Selectors](https://api.jquery.com/category/selectors/)
- [jQuery .attr()](https://api.jquery.com/attr/)

onelinerhub: [How do I use jQuery to get an element by its ID?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-get-an-element-by-its-id)