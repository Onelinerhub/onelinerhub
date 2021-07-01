# Find files newer than 30 seconds

```bash
find /dir -type f -newermt "-30 seconds"
```

- /dir - directory to search files in
- -type f - search only files
- -newermt - filters only files newer than specified timestamp (based on modification time)
- -30 seconds - get only files newer than 30 seconds from now

group: newer_older
