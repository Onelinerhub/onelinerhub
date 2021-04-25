# Insert text into textarea at cursor position

```javascript
var ta = document.querySelector('textarea');
ta.value = ta.value.substring(0, ta.selectionStart)
         + 'Some text'
         + ta.value.substring(ta.selectionEnd, ta.value.length);
```

- document.querySelector('textarea') - query selector for required textarea element
- 'Some text' - this text will be inserted at current cursor position into textarea
