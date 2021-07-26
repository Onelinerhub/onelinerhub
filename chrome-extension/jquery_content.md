# How to add jQuery support to content script in Chrome extension.

```json
{
 "name": "My",
 // ...
 |{|"content_scripts": [
   {
     "matches": ["*://*/*"],
     "js": ["jquery.js", "script.js"]
   }
 ]|}|,
 // ...
}
```

- "name": "My" - name of the extension for `manifest.json`
- matches - on what pages should we load content script
- "\*://\*/\*" - load content script for any page
- jquery.js - [downloaded jquery](https://jquery.com/download/) file
- script.js - name of the script file to load (should be placed in the same dir as `manifest.json`)

group: jquery
