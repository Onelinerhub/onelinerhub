# How to simulate mouse over event on a page

Should be executed in [content script](https://developer.chrome.com/docs/extensions/mv3/content_scripts/),
which is [specified in manifest.json](/chrome-extension/content_script).

```javascript
document.querySelector('div')
.dispatchEvent( new MouseEvent('mouseover', {'bubbles': true})) ;
```

- 'div' - query selector for an element to simulate mouse over on
- dispatchEvent - triggers specified event
- MouseEvent - creates specified mouse event
- mouseover - we need to simulate mouse over
- {'bubbles': true} - event will bubble up the hierarchy of the elements (standard mouseover behaviour)

group: trigger_event
