# Insert text into textarea at cursor position

Will insert ```'Some text'``` text at current cursor position into first ```textarea``` on the page.

```javascript
var ta = document.querySelector('textarea');
ta.value = ta.value.substring(0, ta.selectionStart)
        + 'Some text'
        + ta.value.substring(ta.selectionEnd, ta.value.length);
```
