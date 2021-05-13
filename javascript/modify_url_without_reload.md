# Modify current URL without page reload

```javascript
window.history.pushState({}, '', '/new/url?something');
```

- window.history.pushState - this will change current URL without page reload
- '/new/url?something' - new URL to change current to
