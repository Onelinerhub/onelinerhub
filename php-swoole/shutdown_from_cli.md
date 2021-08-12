# How to shutdown Swoole server from command line.

```bash
pkill -f NAME
```

- pkill - will send SIG_TERM (default signal) to specified processes
- NAME - name of Swoole Master server process

group: shutdown
