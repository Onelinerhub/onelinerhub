# Load persistent background script

No need to specify `persistent` property starting from manifest version `3`:

```json
{
  "name": "My",
  "manifest_version": 3,
  // ...
  |{|"background": {
    "service_worker": "bg.js"
  },|}|,
  // ...
}
```

- "background" - specify scripts to load in background
- "bg.js" - name of the background script to load (should be placed in the same folder as `manifest.json`)

group: background_scripts
