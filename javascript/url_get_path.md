# Get pathname of URL

```javascript
(new URL(some_url)).pathname
```

- `new URL` - create native JS URL object to parse specified URL
- `some_url` - URL to parse
- `pathname` - returns pathname of specified URL

group: url_components

## Example: 
```javascript
console.log( (new URL('https://example.org/test?id=1')).pathname )
```

"/test"
```

group: url_components
```

link_youtube: https://youtu.be/iUaSSQP_S-A
