# Allow cookies permissions

This should be edited in [manifest.json](https://developer.chrome.com/docs/extensions/mv3/manifest/) file.

```json
{
  "name": "My",
  // ...
  |{|"permissions": [
    "cookies",
    "*://*"
   ]|}|,
  // ...
}
```

- permissions - specify extension permissions list
- cookies - allow access to cookies
- "\*://\*" - access cookies on any website
