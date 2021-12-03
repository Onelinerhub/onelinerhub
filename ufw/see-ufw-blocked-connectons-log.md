# See ufw blocked connectons log

```bash
cat /var/log/ufw.log | grep BLOCK
```

- `/var/log/ufw.log` - ufw log file
- `grep BLOCK` - filter only block events

group: log

