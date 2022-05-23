# How to disable GPU

### The `--disable-gpu` is needed on Windows only (and might be removed in future versions):

```bash
google-chrome --headless --disable-gpu --screenshot="screen.png" "https://github.com"
```

- `--screenshot` - make screenshot and save it to specified file
- `--headless` - will launch chrome in [headless mode](https://developers.google.com/web/updates/2017/04/headless-chrome#cli)
- `--disable-gpu` - temporarily needed if running on Windows


