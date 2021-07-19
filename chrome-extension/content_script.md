# Load content script for all pages

```json
{
 "name": "My",
 // ...
 "content_scripts": [
   {
     "matches": ["*://*/*"],
     "js": ["script.js"]
   }
 ],
 // ...
}
```

- "name": "My" - name of the extension for `manifest.json`
- matches - on what pages should we load content script
- "\*://\*/\*" - load content script for any page
- script.js - name of the script file to load (should be placed in the same dir as `manifest.json`)

group: content_scripts
