# How do I use jQuery to append elements to a page?
// plain

jQuery is a JavaScript library that provides a simple way to add, remove, and manipulate HTML elements on a page. To append elements to a page, you can use the `append()` method. This method takes a parameter, which can be either a string of HTML or a jQuery object.

For example, the following code will create a new `<div>` element and append it to the end of the `<body>` element:
```javascript
$('body').append('<div>New Element</div>');
```

The `append()` method can also be used to append a jQuery object to the end of the `<body>` element. For example, the following code will create a new `<div>` element and append it to the end of the `<body>` element:
```javascript
var newElement = $('<div>New Element</div>');
$('body').append(newElement);
```

The `append()` method can also be used to append multiple elements at once. For example, the following code will create three new `<div>` elements and append them to the end of the `<body>` element:
```javascript
$('body').append('<div>Element 1</div><div>Element 2</div><div>Element 3</div>');
```

The parts of the code are:
- `$('body')`: This is a jQuery selector that selects the `<body>` element.
- `append()`: This is the jQuery method that adds elements to the end of the selected element.
- `'<div>Element 1</div><div>Element 2</div><div>Element 3</div>'`: This is a string of HTML that contains three `<div>` elements.

## Helpful links
- [jQuery append() Method](https://www.w3schools.com/jquery/html_append.asp)
- [jQuery Selectors](https://www.w3schools.com/jquery/jquery_selectors.asp)

onelinerhub: [How do I use jQuery to append elements to a page?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-append-elements-to-a-page)