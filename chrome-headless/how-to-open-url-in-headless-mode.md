# How to open URL in headless mode

### Note, that this example will open given URL and exit right away. You might want to [make screenshot](/chrome-headless/how-to-take-page-screenshot), [save page source](/chrome-headless/how-to-save-web-page-source-to-a-file) or [make PDF](/chrome-headless/how-to-save-web-page-to-pdf) out of loaded page.

```bash
google-chrome --headless "https://github.com"
```

- `--headless` - will launch chrome in [headless mode](https://developers.google.com/web/updates/2017/04/headless-chrome#cli)
- `github.com` - url to open


