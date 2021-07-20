# How to download a file

Should be executed in [content script](https://developer.chrome.com/docs/extensions/mv3/content_scripts/),
which is [specified in manifest.json](/chrome-extension/content_script).

```javascript
chrome.downloads.download({ url: "https://example.org/file.txt" });
```

- chrome.downloads.download - downloads a URL
- url: - specify URL to download file from
