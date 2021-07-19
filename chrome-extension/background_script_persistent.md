# Load persistent background script

```json
{
  "name": "My",
  // ...
  |{|"background": {
    "scripts": ["bg.js"],
    "persistent": true
  }|}|,
  // ...
}
```

- "background" - specify scripts to load in background
- "bg.js" - name of the background script to load (should be placed in the same folder as `manifest.json`)
- "persistent": true - enable persistence (to work with [webRequest API](https://developer.chrome.com/docs/extensions/reference/webRequest/))

group: background_scripts
