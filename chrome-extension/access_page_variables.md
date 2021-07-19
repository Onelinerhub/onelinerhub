# How to access page variables

```javascript
var script = document.createElement('script');
script.textContent = 'console.log(page_var);';
(document.head||document.documentElement).appendChild(script);
```

- var script - init script DOM element
- script.textContent - set script content (js code)
- console.log(page_var); - sample code to access page variable (`page_var` is a variable defined within loaded page)
- appendChild(script) - inject script into a page
