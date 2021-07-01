# Find files older than 30 seconds

```bash
find /dir -type f -not -newermt "-30 seconds"
```

- /dir - directory to search files in
- -type f - search only files
- -newermt - filters only files newer than specified timestamp (based on modification time)
- -30 seconds - filter files newer than 30 seconds from now
- -not - reverse search filter (thus, skip all found files and leave only those older than 30 seconds)

group: newer_older
