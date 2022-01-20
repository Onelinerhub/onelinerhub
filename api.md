## API

We're happy to provide our code collection for integrations of all types. At this point, search API is available publicly with no need to register any keys.

Usage is as simple as calling `api.onelinerhub.com/search` endpoint with `query` parameter (GET or POST).

### Example request

```bash
curl "https://api.onelinerhub.com/search?query=php+header+json"
```

### Example response
```javascript
[
  {
    "url": "https:\/\/onelinerhub.com\/javascript\/fetch_post_uri",
    "tech": "javascript",
    "subject": "Ajax post x-www-form-urlencoded data",
    "lang": "javascript",
    "code": "fetch('\/backend.php...log(data);\n});"
  }
  // , ...
]
```


Response data description:
- `url` - public URL of the code piece page
- `tech` - technology of this code
- `subject` - Full title for the code
- `lang` - Code piece language
- `code`- Code piece itself


## Integrations
- [Code search plugin for Visual Studio](https://marketplace.visualstudio.com/items?itemName=pashkatrick.oneliner)
- [oh - search code solutions directly from terminal](http://new.onelinerhub.com/tools)
