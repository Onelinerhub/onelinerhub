# Get hostname by url

```javascript
(new URL(some_url)).hostname
```

- new URL - create native JS URL object to parse specified URL
- some_url - URL to parse
- hostname - returns hostname of specified URL

## Example
```javascript
console.log( (new URL('https://example.org/test?id=1')).hostname )
```
```javascript
"example.org"
```

group: url_components
