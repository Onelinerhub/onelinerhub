# Inject Javascript into webpage from content script

```javascript
var script = document.createElement('script');
script.textContent = 'console.log("Hi");';
(document.head||document.documentElement).appendChild(script);
```

- `document.createElement` - creates script DOM element
- `script.textContent` - script content should be placed here
- `console.log("Hi");` - code we want to inject into page
- `.appendChild(script)` - this is where injection happens

group: inject


link_youtube: https://youtu.be/5upW9YUy5vU
