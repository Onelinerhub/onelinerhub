# Find php.ini loaded by CLI

```bash
php --ini | grep Loaded
```

- --ini - display data on loaded php.ini files
- grep Loaded - filter only main configuration file path
