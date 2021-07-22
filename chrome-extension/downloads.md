# Add downloads permissions

This should be edited in [manifest.json](https://developer.chrome.com/docs/extensions/mv3/manifest/) file.

```json
{
  "name": "My",
  ...
  |{|"permissions": [
    "downloads"
  ]|}|,
  ...
}
```

- permissions - define which permissions our extension will have
- "downloads" - allow extension to launch downloading of files
