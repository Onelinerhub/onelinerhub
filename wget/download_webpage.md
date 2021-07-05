# Download full webpage with it's resources (css, images, ...)

```bash
wget -p -k https://example.org/
```

- -p - will download all resources found on target HTML page
- -k - will change links in downloaded HTML page to load correctly locally
- example.org - example URL to fetch HTML with resouces
