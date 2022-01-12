# How many lines of code from specific author

```bash
git log --author="author" --pretty=tformat: --numstat
```

- `git log` - explore repo log
- `--author` - show only changes by specified author
- `author` - author login/email to count lines for
- `--pretty=tformat: --numstat` - will show only changed files by this author together with changed lines count

group: count

## Example: 
```bash
git log --author="joe" --pretty=tformat: --numstat
```
```
40      0       READMENOT.md
2       0       README.md
```

