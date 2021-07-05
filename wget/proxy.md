# Specify proxy when downloading a file

```bash
wget -e use_proxy=yes -e http_proxy=host:port https://example.ord/file.txt
```

- -e - allows setting configuration parameters
- use_proxy=yes - enabled proxying
- http_proxy=host:port - set proxy host and port
- example.ord/file.txt - file to download
