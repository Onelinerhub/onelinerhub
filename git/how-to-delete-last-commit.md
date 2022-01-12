# How to delete last commit

```bash
git reset --hard HEAD^
```

- `git` - base command
- `reset` - will reset changes accordingly to specified rules
- `--hard` - will actually undo changes in files
- `HEAD^` - return to previous commit

group: delete_commit

## Example: 
```bash
git reset --hard HEAD^
```
```
HEAD is now at a5b9df3 ok
```

