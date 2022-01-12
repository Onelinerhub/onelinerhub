# How to uncommit last commit but keep changes

```bash
git reset HEAD^
```

- `git` - base command
- `reset` - will reset changes accordingly to specified rules
- `HEAD^` - return to previous commit (changed files will keep changes)

group: delete_commit

## Example: 
```bash
git reset HEAD^
```
```
Unstaged changes after reset:
...
```

