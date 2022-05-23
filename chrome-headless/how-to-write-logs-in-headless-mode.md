# How to write logs in headless mode

```bash
google-chrome --headless --enable-logging=stderr --v=1 "https://onelinerhub.com" > logs.log 2>&1
```

- `--headless` - will launch chrome in [headless mode](https://developers.google.com/web/updates/2017/04/headless-chrome#cli)
- `--enable-logging` - configure logging
- `stderr` - write logs to `stderr` output
- `--v=1` - enable verbose mode
- `onelinerhub.com` - sample URL to load on browser launch
- `logs.log` - file to write logs to
- `2>&1` - redirects `stderr` to `stdout` to write all logs to resulting file


