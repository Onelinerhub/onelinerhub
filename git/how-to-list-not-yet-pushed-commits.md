# How to list not yet pushed commits

```bash
git log origin/main..HEAD
```

- `git` - base command
- `log` - will show interactive commits log viewer
- `origin/main` - branch to view unpushed commits from (`main` in our case) 
- `HEAD` - compare everything with current HEAD revision

## Example: 
```bash
git log origin/main..HEAD
```
```
Author: nonunicorn <inonunicorn@gmail.com>
Date:   Tue Jan 11 15:00:46 2022 +0000

    massive content editing update
```

