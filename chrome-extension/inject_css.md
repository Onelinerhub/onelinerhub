# Inject CSS into page

Should be specified in [manifest.json](https://developer.chrome.com/docs/extensions/mv3/manifest/).

```json
{
 "name": "My",
 // ...
 |{|"content_scripts": [
   {
     "matches": ["*://*/*"],
     "css": ["my.css"],
   }
 ]|}|,
 // ...
}
```

- "name": "My" - name of the extension for `manifest.json`
- matches - on what pages should we inject css
- "\*://\*/\*" - inject css into all pages
- my.css - name of the css file to inject (should be placed in the same folder as `manifest.json` file)

group: inject
