# How to execute content script after page content is loaded

```javascript
document.addEventListener('DOMContentLoaded', function() {
  console.log('loaded');
});
```

- `document.addEventListener` - listen for a document event
- `DOMContentLoaded` - event triggers when page is fully loaded
- `console.log('loaded')` - place your code here to execute after page load is complete


link_youtube: https://youtu.be/a2Y04kFQwdg
