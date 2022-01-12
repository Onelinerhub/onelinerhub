# How to rollback to specific commit

```bash
git reset --hard 534d32d
git push -f origin main
```

- `git` - base command
- `reset` - will reset changes accordingly to specified rules
- `--hard` - will actually undo changes in files
- `534d32d` - commit to roll back to
- `git push -f` - force push (because we're changing something in the past)
- `origin` - remote name
- `main` - branch name (master name in our case)


