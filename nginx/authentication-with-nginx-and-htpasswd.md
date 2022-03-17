# Authentication with Nginx and htpasswd

```nginx
server {
  location /admin {
    auth_basic “For chosen only”;
    auth_basic_user_file /etc/nginx/.htpasswd; 
  }
}
```

- `server {` - virtual server configuration block
- `/admin` - example location to restrict with password
- `auth_basic` - enables HTTP authentication
- `“For chosen only”` - message before asking for password
- `auth_basic_user_file` - set file path to generated [htpasswd](/htpasswd/create) file
- `/etc/nginx/.htpasswd` - generated [htpasswd](/htpasswd/create) file


