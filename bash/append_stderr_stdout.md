# How to append stderr to stdout and log it to a file

```bash
cmd >> log.txt 2>&1
```

- cmd - command which output we're going to log
- >> log.txt - will write output to ```log.txt```
- 2>&1 - will redirect stderr to the same output
