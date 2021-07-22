# Set extension icon

This should be edited in [manifest.json](https://developer.chrome.com/docs/extensions/mv3/manifest/) file.

```json
{
  "name": "My",
  // ...
  |{|"icons": {
    "16": "icon16.png",
    "48": "icon48.png",
    "128": "icon128.png"
  },|}|,
  // ...
}
```

- 16 - specify path to 16x16 icon, `icon16.png` should be placed in the same directory as manifest.json
- 48 - specify path to 48x48 icon
- 128 - specify path to 128x128 icon
