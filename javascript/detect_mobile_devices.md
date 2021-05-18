# Detect mobile device

```javascript
var mobile = window.matchMedia("only screen and (max-width: 760px)").matches;
```

- mobile - will contain ```true``` if screen width is smaller than ```760px``` ([why is this better than user agent?](https://stackoverflow.com/questions/3514784/what-is-the-best-way-to-detect-a-mobile-device))
- window.matchMedia - check CSS defined rule for media
