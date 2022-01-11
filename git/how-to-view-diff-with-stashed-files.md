# How to view diff with stashed files

```bash
git diff stash
```

- `git` - base command
- `diff` - will show diff of the specified entities
- `stash` - will show diff of current and stashed files

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

