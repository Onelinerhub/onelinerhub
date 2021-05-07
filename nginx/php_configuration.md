# The simplest PHP configuration

```nginx
server {
  server_name server.com;
  root /var/server.com;
  index index.php;

  location ~ \.php$ {
    include snippets/fastcgi-php.conf;
    fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
  }
}
```

- index index.php - launch index.php file by default
- \.php$ - regex to intercept all php files
- snippets/fastcgi-php.conf - fastcgi configuration snippet
- /var/run/php/php7.4-fpm.sock - path to your fpm socket (check your version)
