# How to find text in files

```bash
grep -m 1 'text' *.txt | head -1
```

- -m 1 - stop searching current file after first match
- 'text' - text to search
- *.txt - search in all ```txt``` files of current dir
- head -1 - will print only first found result (replace ```1``` with any number of results you want to have)
