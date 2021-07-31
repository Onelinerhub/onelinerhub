# Add context menu permissions

This should be edited in [manifest.json](https://developer.chrome.com/docs/extensions/mv3/manifest/) file.

```json
{
  "name": "My",
  // ...
  |{|"permissions": [
    "contextMenus"
   ]|}|,
  // ...
}
```

- permissions - specify extension permissions list
- contextMenus - allow access to context menu
