# How many lines of code are there in a repo

```bash
git ls-files | xargs wc -l
```

- `git ls-files` - list all files in current repo
- `xargs wc -l` - count lines in each file an print total

group: count

## Example: 
```bash
git ls-files | xargs wc -l
```
```
  1 .gitignore
  2 README.md
  6 file.txt
  9 total

```

