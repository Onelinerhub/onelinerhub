# element

How do I select the next element with jQuery?
// plain

The jQuery `.next()` method can be used to select the next element relative to the selected element.

For example, the following code will select the next `<p>` element after the `<h1>` element:

```
$('h1').next('p');
```

The `.next()` method takes an optional argument which is a selector string. This can be used to filter the selection to a specific element type.

The following code will select the next `<div>` element after the `<h1>` element:

```
$('h1').next('div');
```

The `.next()` method will only select the immediately following element. If you need to select multiple elements then you can use the `.nextAll()` method which takes a selector string as an optional argument.

The following code will select all `<p>` elements after the `<h1>` element:

```
$('h1').nextAll('p');
```

The `.next()` and `.nextAll()` methods are useful for selecting elements relative to the currently selected element.

## Helpful links
- [jQuery .next() Documentation](https://api.jquery.com/next/)
- [jQuery .nextAll() Documentation](https://api.jquery.com/nextAll/)

onelinerhub: [element

How do I select the next element with jQuery?](https://onelinerhub.com/jquery/element--how-do-i-select-the-next-element-with-jquery)