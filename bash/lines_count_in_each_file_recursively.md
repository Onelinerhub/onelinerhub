# How to show lines count in files recursively

```bash
find /tmp -name '*.txt' -print0 | xargs -0 wc -l
```

- `/tmp` - directory to fund files in
- `-name '*.txt'` - search only for ```.txt``` extension
- `xargs -0 wc -l` - will show line number for each found file

group: lines_count_in_files


link_youtube: https://youtu.be/D4M2X8VknWw
