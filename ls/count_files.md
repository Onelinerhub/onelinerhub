# Count number of files in a directory

```bash
ls -1 /tmp | wc -l
```

- /tmp - directory to count files in (including subdirectories)
- -1 - ensure there's only one line per file
- wc -l - count number of lines outputted by ```ls``` (thus, number of files)
