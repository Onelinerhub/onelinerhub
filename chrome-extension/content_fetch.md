# How to fetch data in content script

```javascript
fetch('https://example.org/some')
.then(response => response.text())
.then(response => console.log(response))
```

- `example.org/some` - sample url to fetch data from
- `esponse.text()` - let's assume we're fetching text data
- `console.log(response)` - do something with response

group: fetch_data


link_youtube: https://youtu.be/0Lsfq8IxUds
