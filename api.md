## API

We're happy to provide our code collection for integrations of all types. At this point, search API is available publicly with no need to register any keys.

Usage is as simple as calling `api.onelinerhub.com/search` endpoint with `quqery` parameter (GET or POST):

```bash
curl "https://api.onelinerhub.com/search?query=php+header+json"
```

You'll get JSON array with the following objects:
```json
{
  "url": "...", // public URL of the code piece page
  "tech": "...", // technology of this code
  "subject": "...", // Full title for the code
  "lang": "...", // Code piece language
  "code": "..." // Code piece itself
}
```

Example:
```json
[
    {
        "url": "https:\/\/onelinerhub.com\/javascript\/fetch_post_uri",
        "tech": "javascript",
        "subject": "Ajax post x-www-form-urlencoded data",
        "lang": "javascript",
        "code": "fetch('\/backend.php', {\n  method: 'post',\n  headers: { 'Content-Type': 'application\/x-www-form-urlencoded;charset=UTF-8' },\n  body: 'var1=' + encodeURIComponent('Donald Trump :(') + '&amp;var2=123'\n}).then(function(r) {\n  return r.json();\n}).then(function(data) {\n  console.log(data);\n});"
    },
    {
        "url": "https:\/\/onelinerhub.com\/php\/json_content_type",
        "tech": "php",
        "subject": "Set content type to JSON",
        "lang": "php",
        "code": "header('Content-Type: application\/json');\necho json_encode([]);"
    }
]
```


## Integrations

- [Visual Studio plugin](https://marketplace.visualstudio.com/items?itemName=pashkatrick.oneliner)
