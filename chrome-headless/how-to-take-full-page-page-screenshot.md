# How to take full page page screenshot

### There is no automatic way to detect loaded page height, but you can set big height value of `-window-size` option to grab full pages screenshots:

```bash
google-chrome --headless --screenshot="screen.png" -window-size=1280,8000 "https://github.com"
```

- `--headless` - will launch chrome in [headless mode](https://developers.google.com/web/updates/2017/04/headless-chrome#cli)
- `--screenshot` - make screenshot and save it to specified file
- `screen.png` - path to save screenshot to
- `-window-size` - set browser window size
- `1280,8000` - we use `8000` for browser height to get full page screenshot
- `github.com` - url to open

group: screenshot


