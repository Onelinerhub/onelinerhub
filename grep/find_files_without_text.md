# How to find files that do not contain specific text

```bash
grep -L 'text' *.txt
```

- 'text' - text to match against
- -L - asks grep to show files that do not contain text (use ```-Lr``` for recursive search)
- *.txt - check all ```txt``` files in current directory
