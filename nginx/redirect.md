# How to redirect

```nginx
location / {
  rewrite ^/some_url /some_other_url permanent;
}
```

- /some_url - redirect from this url
- /some_other_url - redirect to this url
