# How to join (squash) two commits

```bash
git rebase -i HEAD~2

# p fe5592f ok
# s b35b6b8 ok
```

- `git rebase` - rebase within current repo
- `-i` - interactive editor
- `HEAD~2` - join 2 last commits
- ` p ` - in the editor, set first commit with `p` (start of the line)
- ` s ` - second and all other commits should be changed to `s`


