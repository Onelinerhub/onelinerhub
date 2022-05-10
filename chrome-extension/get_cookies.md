# Get cookie value

```javascript
chrome.cookies.get({"url": 'https://example.org', "name": 'test'}, function(cookie) {
  console.log(cookie.value);
});
```

- `chrome.cookies` - API to manipulate cookies
- `example.org` - domain to get cookies for
- `test` - name of a cookie to get value for
- `console.log(cookie.value)` - do something with this cookie value

group: cookies


link_youtube: https://youtu.be/KnVGFyvP2xU
