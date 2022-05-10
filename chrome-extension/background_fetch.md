# How to fetch data in background script

```javascript
fetch('https://example.org/some')
.then(response => response.text())
.then(response => console.log(response))
.catch()
```

- `example.org/some` - sample url to fetch data from
- `esponse.text()` - let's assume we're fetching text data
- `console.log(response)` - do something with response
- `catch()` - intercept all possible errors, so it won't break execution

group: fetch_data


link_youtube: https://youtu.be/nqfAinW7bR0
