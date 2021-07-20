# How to fetch data in content script

Should be executed in [content script](https://developer.chrome.com/docs/extensions/mv3/content_scripts/),
which is [specified in manifest.json](/chrome-extension/content_script).

```javascript
fetch('https://example.org/some')
.then(response => response.text())
.then(response => console.log(response))
```

- example.org/some - sample url to fetch data from
- esponse.text() - let's assume we're fetching text data
- console.log(response) - do something with response

group: fetch_data
