# How to undo "git add" on all files before commit

```bash
git reset HEAD -- .
```

- `HEAD` - points to current branch. change it if yours is diffrent.
- `.` - will unstage all added files/folders

group: undo_add


