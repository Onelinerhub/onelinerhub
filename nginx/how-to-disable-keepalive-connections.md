# How to disable keepalive connections

```nginx
server {
  keepalive_timeout 0;
}
```

- `server {` - virtual server configuration block
- `keepalive_timeout 0` - set this to zero to disable keep-alive connections

group: keepalive


link_youtube: https://youtu.be/B0rlwT6OoWw
