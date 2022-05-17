# Change directory and all dependencies permissions

```bash
find /home/usr/ -type d -exec chmod 777 {} \;
```

- `/home/usr/` - Base path to change permissions.
- `-type d` - Search for directories (affects files too).
- `-exec` - Execute next command.
- `chmod 777` - Grants all permissions to all users (See [how to pick numbers](/bash/chmod)).
- `{}` - Will be replaced by the path.
- `\;` - Denotes the end of command.


link_youtube: https://youtu.be/ZYl60KrET3A
