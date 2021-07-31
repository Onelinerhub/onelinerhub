# Defining public resources using web_accessible_resources

This should be edited in [manifest.json](https://developer.chrome.com/docs/extensions/mv3/manifest/) file.

```json
{
  "name": "My",
  // ...
  |{|"web_accessible_resources": [
    {
      "resources": [ 'img.png' ],
      "matches": [ '*://*/*' ]
    }
   ]|}|,
  // ...
}
```

- web_accessible_resources - definses a list of extension resources to be accessed through web
- 'img.png' - image file (placed inside extension folder) to be accessed through web
- '\*://\*/\*' - grant access for any website
