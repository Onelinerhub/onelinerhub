# Document ready callback (jquery $(document).ready equivalent)

```javascript
document.addEventListener('DOMContentLoaded', function(event) { 
  console.log('Content loaded');
});
```

- document.addEventListener - adds new event listener
- DOMContentLoaded - fired when html was parsed but styles/images/videos not yet loaded ([details](https://developer.mozilla.org/en-US/docs/Web/API/Window/DOMContentLoaded_event))
- console.log('Content loaded') - replace with your code to run when document was loaded
