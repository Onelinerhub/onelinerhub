# Using rewrite rules

```nginx
server {
  rewrite ^/files/(.+)$ /download.php?file=$1 last;
}
```

- `server {` - virtual server configuration block
- `rewrite` - define URL rewrite rule
- `^/files/(.+)$` - sample regex to match URI for rewrite
- `/download.php?file=$1` - resulting URL to rewrite request to (`$1` is captured from previous regex)
- `last` - stop checking next rewrite rules (if there are any) after this one


