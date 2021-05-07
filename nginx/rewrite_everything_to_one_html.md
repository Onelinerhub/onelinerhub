# Rewrite all requests to one single file

```nginx
location / {
  try_files /one.html =404;
}
```

- try_files - this directive will try to server listed files/rules
- /one.html - since we have only this file, it will be server for all requests
- =404 - this tells Nginx to not look for other files on a disk
