# How to keep running Chrome in headless mode

### In order to keep running, we should enable [debugging port](/), so Chrome knows we want it to stay:

```bash
google-chrome --headless --remote-debugging-port=9222 "https://onelinerhub.com/"
```

- `--headless` - will launch chrome in [headless mode](https://developers.google.com/web/updates/2017/04/headless-chrome#cli)
- `--remote-debugging-port` - specify port to listen for [debugging protocol](/chrome-headless/chrome-remote-interface-usage-example)
- `onelinerhub.com` - open this URL in browser

group: remote-debugging


