# Search for files and directories and remove them

```bash
find /tmp -exec rm -rf {} \;
```

- `/tmp` - base path to search in
- `-exec` - execute specified command for each found file or directory
- `rm -rf {}` - this command will be executed for each file/dir

group: find_remove


link_youtube: https://youtu.be/cenzVECbXwI
