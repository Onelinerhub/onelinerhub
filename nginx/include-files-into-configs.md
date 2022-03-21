# Include file into config

```nginx
server {
  include /etc/nginx/websites/my1.conf;
}
```

- `server {` - virtual server configuration block
- `include` - include specified configuration file
- `/etc/nginx/websites/my1.conf` - sample config file to include

group: config


