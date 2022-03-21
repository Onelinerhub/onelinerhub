# Using map

### This example demonstrates redirecting old website to new and mapping old URLs to new using `map` rules:

```nginx
map $uri $new_uri {
  default /;
  /old_article /new_article;
}

server {
  rewrite ^ https://new.com$new_uri permanent;
}
```

- `map` - define variables map 
- `$uri $new_uri` - will generate `$new_uri` variable value based on `$uri` and map rules
- `default /;` - by default `$new_uri` will contain `/` value
- `/old_article /new_article` - if `/old_article` request is made, `$new_uri` variable will get `/new_article` value
- `server {` - virtual server configuration block
- `rewrite` - define URL rewrite rule
- `^ https://new.com$new_uri` - rewrite all URLs to 
- `permanent` - will make browser redirect instead of silent rewrite

group: map


