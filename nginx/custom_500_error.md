# Custom 500 (internal) errors page

```nginx
error_page 500 502 503 504 /my500.html;
```

- error_page - defines custom page to show on error identified by a code
- 500 502 503 504 - list of internal error codes
- /my500.html - path to custom page to show on internal errors

group: custom_error_page
