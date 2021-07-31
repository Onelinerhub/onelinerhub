# Extension permissions declaration and list for Chrome.

This should be edited in [manifest.json](https://developer.chrome.com/docs/extensions/mv3/manifest/) file.

```json
{
  "name": "My",
  // ...
  |{|"permissions": [
    "cookies",
    // other permissions
   ]|}|,
  // ...
}
```

- permissions - specify extension permissions list
- cookies - allow access to cookies
- other permissions - see [full permission list](https://developer.chrome.com/docs/extensions/mv3/declare_permissions/)
