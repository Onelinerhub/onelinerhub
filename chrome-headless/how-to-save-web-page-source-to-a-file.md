# How to save web page source to a file

```bash
google-chrome --headless --dump-dom "https://github.com" > source.html
```

- `--headless` - will launch chrome in [headless mode](https://developers.google.com/web/updates/2017/04/headless-chrome#cli)
- `--dump-dom` - will print loaded URL source
- `github.com` - url to open
- `source.html` - path to file to save output html to


