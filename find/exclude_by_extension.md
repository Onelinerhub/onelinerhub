# Search for files excluding certain extension

```bash
find /tmp -type f -not -name "*.xls"
```

- `/tmp` - base path to search in
- `-type f` - locate only files (skip directories)
- `-not` - will revert next rule
- `-name "\*.xls"` - match all Excel files (thus exclude them from results)


link_youtube: https://youtu.be/_bSy3Xyq_TU
