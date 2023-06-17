# How do I use jQuery to set the position of an element on a web page?
// plain

To use jQuery to set the position of an element on a web page, you can use the `offset()` method. This method takes two parameters - left and top - which represent the left and top positions of the element relative to the document.

For example, the following code will set the position of an element with an ID of `myElement` to `left: 200px; top: 100px;`:
```javascript
$('#myElement').offset({ left: 200, top: 100 });
```

## Code explanation

- `$('#myElement')`: selects the element with an ID of `myElement`
- `offset()`: sets the position of the element
- `{ left: 200, top: 100 }`: the left and top positions of the element relative to the document

## Helpful links
- [jQuery offset() Method](https://www.w3schools.com/jquery/jquery_offset.asp)

onelinerhub: [How do I use jQuery to set the position of an element on a web page?](https://onelinerhub.com/jquery/how-do-i-use-jquery-to-set-the-position-of-an-element-on-a-web-page)