# How many commits are there in a branch

```bash
git rev-list --count branch
```

- `git` - base command
- `rev-list` - get revisions
- `--count` - only print revisions count
- `branch` - branch name to count commits for

## Example: 
```bash
git rev-list --count test1
```
```
2
```

