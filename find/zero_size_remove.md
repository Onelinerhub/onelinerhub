# Search for files of zero size and remove them

```bash
find /var/log -size 0 -delete
```

- /var/log - directory to search inside
- -size 0 - will locate all zero-sized files
- -delete - will remove found files

group: zero_size
