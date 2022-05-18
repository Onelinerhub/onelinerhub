# Exclude certain directories when doing recusrive search

```bash
grep -r 'text' --exclude-dir={dir1,dir2} /path/to/search/
```

- `-r` - use recursive search 
- `'text'` - text to search
- `dir1,dir2` - skip ```dir1``` and ```dir2``` directories when searching
- `/path/to/search/` - directory to search in


link_youtube: https://youtu.be/lbuqHfxwODY
