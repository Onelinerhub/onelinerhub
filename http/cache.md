# HTTP headers to cache HTML, CSS, JS or images.

```bash
Cache-Control: public
Expires: Wed, 21 Oct 2045 07:28:00 GMT
```

- Cache-Control: - specify cache rules for browser
- no-store, must-revalidate - ask browser to not save any cached versions and request fresh versions each time
- Expires: - sets cache expiration date (so the browser will request a fresh version after that date)
