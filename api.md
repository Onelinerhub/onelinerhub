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
    "code": "fetch('\/backend.php', {\n  method: 'post',\n  headers: { 'Content-Type': 'application\/x-www-form-urlencoded;charset=UTF-8' },\n  body: 'var1=' + encodeURIComponent('Donald Trump :(') + '&amp;var2=123'\n}).then(function(r) {\n  return r.json();\n}).then(function(data) {\n  console.log(data);\n});"
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
