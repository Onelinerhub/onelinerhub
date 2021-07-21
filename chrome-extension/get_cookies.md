# Get cookie value

Should be executed in [background script](https://developer.chrome.com/docs/extensions/mv3/background_pages/),
which is [specified in manifest.json](/chrome-extension/background_script).
Also [cookies persmissions](/chrome-extension/cookies) should be set.

```javascript
chrome.cookies.get({"url": 'https://example.org', "name": 'test'}, function(cookie) {
  console.log(cookie.value);
});
```

- chrome.cookies - API to manipulate cookies
- example.org - domain to get cookies for
- test - name of a cookie to get value for
- console.log(cookie.value) - do something with this cookie value
