# How to kill process by port

```bash
sudo kill `sudo lsof -t -i:8123`
```

- `sudo` - execute command as super user (root)
- `kill` - will kill specified process
- `lsof -t -i:8123` - will list all processes listening on `8123` port

group: kill


