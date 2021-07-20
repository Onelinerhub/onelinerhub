# Load background script

```json
{
  "name": "My",
  // ...
  |{|"background": {
    "scripts": ["bg.js"],
    "persistent": false
  }|}|,
  // ...
}
```

- "background" - specify scripts to load in background
- "bg.js" - name of the background script to load (should be placed in the same folder as `manifest.json`)

group: background_scripts
