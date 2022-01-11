# How to unstash changes

```bash
git stash pop
```

- `git` - base command
- `stash` - manage stash storage
- `pop` - get all stashed changes and put it back to a local repo

group: stash

## Example: 
```bash
git diff stash
```
```
diff --git a/test b/test
new file mode 100644
index 0000000..32aad8c
--- /dev/null
+++ b/test
@@ -0,0 +1 @@
+hi!

```

