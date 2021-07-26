# How to simulate keypress/keyup/keydown event on a page

Should be executed in [content script](https://developer.chrome.com/docs/extensions/mv3/content_scripts/),
which is [specified in manifest.json](/chrome-extension/content_script).

```javascript
document.querySelector('input')
.dispatchEvent(new KeyboardEvent('keyup', {'key': 'a'}));
```

- 'div' - query selector for an element to simulate mouse over on
- dispatchEvent - triggers specified event
- KeyboardEvent - creates specified key event
- keyup - we want to simulate keyup event
- 'key': 'a' - simulate `a` key press (all [keys list](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values))

group: trigger_event
