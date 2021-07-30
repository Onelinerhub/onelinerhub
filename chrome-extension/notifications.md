# Allow notifications permissions

This should be edited in [manifest.json](https://developer.chrome.com/docs/extensions/mv3/manifest/) file.

```json
{
  "name": "My",
  // ...
  |{|"permissions": [
    "notifications"
   ]|}|,
  // ...
}
```

- permissions - specify extension permissions list
- notifications - enable [notifications API](https://developer.chrome.com/docs/extensions/reference/notifications/) permissions

group: notification
