# Set cookie value

Should be executed in [background script](https://developer.chrome.com/docs/extensions/mv3/background_pages/),
which is [specified in manifest.json](/chrome-extension/background_script).
Also [cookies persmissions](/chrome-extension/cookies) should be set.

```javascript
chrome.cookies.set({url: 'https://example.org', name: 'test', value: 'x'});
```

- chrome.cookies - API to manipulate cookies
- example.org - domain to set cookie for
- test - name of a cookie to set value for
- 'x' - value of the cookie to set

group: cookies
