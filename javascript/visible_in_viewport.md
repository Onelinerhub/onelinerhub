# CHeck if DOM element is visible in current viewport

```javascript
var el = document.querySelector('div');
var rect = el.getBoundingClientRect();
var is_visible = rect.top >= 0 && rect.left >= 0 &&
                 rect.bottom <= (window.innerHeight || document.documentElement.clientHeight) &&
                 rect.right <= (window.innerWidth || document.documentElement.clientWidth);
```

- document.querySelector('div') - select needed DOM element
- el.getBoundingClientRect() - [gets element coordinates](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect) relative to viewport
- is_visible - will contain ```true``` if element is visible in the current viewport
