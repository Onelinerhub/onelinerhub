# How do I access the children of an element using jQuery?
// plain

You can access the children of an element using jQuery's `.children()` method.

The `.children()` method returns all direct children of the selected element.

For example, given the following HTML:
```
<div id="parent">
  <p>Paragraph 1</p>
  <p>Paragraph 2</p>
  <div>
    <p>Paragraph 3</p>
  </div>
</div>
```

You can access the children of the element with id `parent` using the following jQuery code:
```
var children = $('#parent').children();
```

The `children` variable will contain a collection of all direct children of the element with id `parent`, in this case two `<p>` elements and one `<div>` element.

You can also use the `.children()` method with a selector to limit the returned elements. For example, the following code will return only the `<p>` elements as children of the element with id `parent`:
```
var paragraphs = $('#parent').children('p');
```

## Helpful links
- [jQuery API Documentation - .children()](https://api.jquery.com/children/)

onelinerhub: [How do I access the children of an element using jQuery?](https://onelinerhub.com/jquery/how-do-i-access-the-children-of-an-element-using-jquery)