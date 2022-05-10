# How to add jQuery support to background script in Chrome extension.

```json
{
 "name": "My",
 // ...
 "background": {
    "scripts": ["jquery.js", "bg.js"],
    "persistent": false
  },,
 // ...
}
```

- `"name": "My"` - name of the extension for `manifest.json`
- `jquery.js` - [downloaded jquery](https://jquery.com/download/) file
- `bg.js` - name of the script file to load (should be placed in the same dir as `manifest.json`)

group: jquery


link_youtube: https://youtu.be/yxd41F7944E
