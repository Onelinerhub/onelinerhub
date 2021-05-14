# Get selected option text of a dropdown (select) box

```javascript
var sel = document.querySelector('select');
var selected = sel.options[sel.selectedIndex].text;
```

- var sel = document.querySelector('select') - selects needed ```select``` element
- var selected - will contain selected option text
- sel.selectedIndex - returns selected option index
- sel.options - array with ```select``` options
