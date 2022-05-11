# How to access or modify window object

```javascript
var script = document.createElement('script');
script.textContent = 'console.log(window);';
(document.head||document.documentElement).appendChild(script);
```

- `var script` - init script DOM element
- `script.textContent` - set script content (js code)
- `console.log(window);` - place your window object manipulation code here
- `appendChild(script)` - inject script into a page


link_youtube: https://youtu.be/k4qkQwkcNhw
