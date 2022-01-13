# How to count all lines in all files recursively

```bash
( find /tmp -name '*.txt' -print0 | xargs -0 cat ) | wc -l
```

- `/tmp` - directory to fund files in
- `-name '*.txt'` - search only for ```.txt``` extension
- `xargs -0 cat` - will first print all files inside the command itself
- `wc -l` - will count all lines in all files as a single final numer

group: lines_count_in_files


link_youtube: https://youtu.be/UBPGlBAUQhA
