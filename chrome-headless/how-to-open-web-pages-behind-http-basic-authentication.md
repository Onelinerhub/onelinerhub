# How to open web pages behind HTTP basic authentication

```bash
google-chrome --headless "https://user:pwd@server.com"
```

- `--headless` - will launch chrome in [headless mode](https://developers.google.com/web/updates/2017/04/headless-chrome#cli)
- `user:pwd` - HTTP basic auth credentials
- `server.com` - URL to open


