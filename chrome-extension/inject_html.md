# Inject HTML into page

```javascript
var div = document.createElement('div'); 
div.innerHTML = '<b>Hi!</b>';
document.body.appendChild(div);
```

- `var div` - init div DOM element
- `div.innerHTML` - set HTML for new div
- `document.body.appendChild(div)` - inject new div (with our HTML code) into current page

group: inject


link_youtube: https://youtu.be/IH-wc-uSVu8
