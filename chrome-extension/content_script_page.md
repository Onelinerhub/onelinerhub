# Load content script for specific pages

```json
{
 "name": "My",
 ...
 "content_scripts": [
   {
     "matches": ["https://example.org/*"],
     "js": ["script.js"]
   }
 ],
 ...
}
```

- "name": "My" - name of the extension for `manifest.json`
- matches - on what pages should we load content script
- "https://example.org/\*" - load content script all pages of `example.org` domain
- script.js - name of the script file to load (should be placed in the same dir as `manifest.json`)

group: content_scripts
