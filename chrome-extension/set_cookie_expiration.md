# Set cookie value and expiration time

Should be executed in [background script](https://developer.chrome.com/docs/extensions/mv3/background_pages/),
which is [specified in manifest.json](/chrome-extension/background_script).
Also [cookies persmissions](/chrome-extension/cookies) should be set.

```javascript
chrome.cookies.set({url: 'https://example.org', name: 'test', value: 'x', expirationDate: (new Date().getTime()/1000) + 60 * 60 * 24 * 30});
```

- chrome.cookies - API to manipulate cookies
- example.org - domain to set cookie for
- test - name of a cookie to set value for
- 'x' - value of the cookie to set
- expirationDate - sets expiration time for cookie (number of seconds since the UNIX epoch)
- new Date().getTime()/1000) - current UNIX time
- 60 * 60 * 24 * 30 - cookie will expire in 30 days

group: cookies
