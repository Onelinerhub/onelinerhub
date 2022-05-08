# How to set referer

```bash
curl -e "https://google.com" https://example.org
```

- `curl` - base curl command
- `-e` - sets specified referer for the request
- `https://google.com` - use this as a referer 
- `https://example.org` - sample URL to send request to

## Example: 
```bash
curl -e "https://google.com" https://httpbin.org/anything | grep referer
```
```
"Referer": "https://google.com", 
```

link_youtube: https://youtu.be/eUaln3b1UlA
