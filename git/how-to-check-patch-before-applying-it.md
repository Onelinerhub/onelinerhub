# How to check patch (dry-run) before applying it

```bash
git apply --stat name.patch
git apply --check name.patch
```

- `git` - base command
- `apply` - applies specified patch to current repo
- `name.patch` - name of the patch file
- `--stat` - show patch stats without any actual changes
- `--check` - check patch for errors without actual changes

group: patch


