# Using try_files

```nginx
server {
  root /var/www/example;
  location / {
    try_files $uri $uri/ /index.php;
  }
}
```

- `server {` - virtual server configuration block
- `location / {` - default location block
- `try_files` - try serving from specified paths 
- `$uri $uri/` - try to serve either file or folder named as request
- `/index.php` - if previous checks fails server `index.php` file from root folder


