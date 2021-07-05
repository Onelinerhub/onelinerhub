# HTTP headers to disable browser caching.

```bash
Cache-Control: no-store, must-revalidate
Expires: 0
```

- Cache-Control: - specify cache rules for browser
- no-store, must-revalidate - ask browser to not save any cached versions and request fresh versions each time
- Expires: 0 - aditionally tell browser that cache expiration time is zero
