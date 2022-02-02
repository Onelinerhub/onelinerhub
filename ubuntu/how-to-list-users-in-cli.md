# How to list users in CLI

```bash
cat /etc/passwd
```

- `cat` - print contents of specified file
- `/etc/passwd` - all system users reside in this file

## Example: 
```bash
cat /etc/passwd
```
```
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
...
```

