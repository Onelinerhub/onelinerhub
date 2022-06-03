# How far is branch behind master

```bash
git rev-list --left-right --count main...branch1
# 7         1
# ^         ^
# behind    ahead of
# master    master
```

- `git` - base command
- `rev-list` - get revisions
- `--left-right --count` - outputs counts: left for master and right for branch
- `main` - name of the master branch
- `branch1` - name of the branch to compare with master

## Example: 
```bash
git rev-list --left-right --count main...branch1
```
```
7	1
```

link_youtube: https://youtu.be/0B6zkx6Kzmw
