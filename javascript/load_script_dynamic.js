# How to load script dynamically on a web page

```javascript
var script = document.createElement('script');
script.src = '/script.js';
document.head.appendChild(script);
```

- document.createElement - will create script node
- /script.js - url of the js script to load
- document.head.appendChild - will insert script node into DOM
