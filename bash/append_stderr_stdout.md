# How to append stderr to stdout and log it to a file

```bash
cmd >> log.txt 2>&1
```

- `cmd` - command which output we're going to log
- `log.txt` - we will append output to ```log.txt``` file
- `2>&1` - will redirect stderr to the same output


link_youtube: https://www.youtube.com/watch?v=BWpPrsa67V8
