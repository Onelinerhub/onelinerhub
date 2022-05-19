# How to save web page to PDF

```bash
google-chrome --headless --print-to-pdf="screen.pdf" -window-size=1280,720 "https://github.com"
```

- `--headless` - will launch chrome in [headless mode](https://developers.google.com/web/updates/2017/04/headless-chrome#cli)
- `--print-to-pdf` - generate PDF from loaded URL and save it to specified file
- `screen.pdf` - name of the PDF file to save output to
- `-window-size` - set browser window size
- `1280,720` - opens browser in `1280x720` size
- `github.com` - url to open


