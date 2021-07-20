# Get pathname of URL

```javascript
(new URL(some_url)).pathname
```

- new URL - create native JS URL object to parse specified URL
- some_url - URL to parse
- pathname - returns pathname of specified URL

## Example
```javascript
console.log( (new URL('https://example.org/test?id=1')).pathname )
```
```javascript
"/test"
```

group: url_components
