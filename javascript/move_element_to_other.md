# How to move an element into another element

```javascript
document.querySelector('#parent').appendChild( document.querySelector('#child') );
```

- document.querySelector('#child') - selects element to append to new element
- document.querySelector('#parent') - selects element to append child element to
- appendChild - appends element in arguments to selected element
