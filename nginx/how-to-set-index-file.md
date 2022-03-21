# How to set index file

```nginx
server {
  index default.php;
}
```

- `server {` - virtual server configuration block
- `index` - sets default file to serve if request is `/`
- `default.php` - serve this file as default file (index file)


