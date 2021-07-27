# Manifest V3 example for Chrome extension.

```json
{
  "name": "My",
  "version": "1.2.3",
  "manifest_version": 3,
  "background": {
    "service_worker": "bg.js"
  },
  "content_scripts": [
    {
      "matches": [ "*://*/*" ],
      "all_frames": true,
      "js": ["content.js"]
    }
  ]
}
```

- "name" - title for our extension
- "version" - version of our extension
- "manifest_version": 3 - v3 format
- bg.js - background script (worker) to load
- content.js - content script to load
- "*://*/*" - load content script on all pages
- all_frames": true - load content script in all frames
