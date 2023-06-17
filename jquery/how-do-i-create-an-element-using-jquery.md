# How do I create an element using jQuery?
// plain

jQuery provides a simple and straightforward way to create elements. The following example code creates a `<div>` element and appends it to the `<body>` of the page.

```
$('<div/>', {
    id: 'myDiv',
    text: 'My div'
}).appendTo('body');
```

This will create a `<div>` element with an `id` of `myDiv` and text content of `My div`, and append it to the `<body>` element.

The parts of the code are as follows:

* `$('<div/>')` creates a new `<div>` element.
* `{ id: 'myDiv', text: 'My div' }` is an object containing the properties for the element, in this case `id` and `text`.
* `.appendTo('body')` adds the element to the `<body>` element.

## Helpful links

* [jQuery Documentation - Creating New Elements](https://api.jquery.com/jQuery/#jQuery2)
* [jQuery Documentation - .appendTo()](https://api.jquery.com/appendTo/)

onelinerhub: [How do I create an element using jQuery?](https://onelinerhub.com/jquery/how-do-i-create-an-element-using-jquery)