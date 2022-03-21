# Using Letsencrypt with Nginx

### Consider using [Certbot Nginx script](/certbot/creating_ssl_certificate_for_nginx) to automatically configure SSL for your web app:

```nginx
server {
  server_name domain.com;
  listen 443 ssl;

  ssl_certificate /etc/letsencrypt/live/domain.com/fullchain.pem;
  ssl_certificate_key /etc/letsencrypt/live/domain.com/privkey.pem;

  include /etc/letsencrypt/options-ssl-nginx.conf;
}
```

- `server {` - virtual server configuration block
- `listen 443 ssl` - enable SSL
- `domain.com` - example domain to enable Letsencrypt SSL for
- `fullchain.pem` - [generated certificate](/certbot/create_standalone_certificate) file
- `privkey.pem` - [generated certificate](/certbot/create_standalone_certificate) key


