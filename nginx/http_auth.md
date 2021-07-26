# Basic HTTP authentication

```nginx
location / {
  auth_basic "No no no";
  auth_basic_user_file /dir/.htpasswd; 
}
```

- auth_basic - message to display when auth dialog pops up
- auth_basic_user_file - specifies user/password file path
- /dir/.htpasswd - read how to create [htpasswd format file](/htpasswd/create)
