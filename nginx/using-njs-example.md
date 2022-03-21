# Using NJs example

```nginx
js_import test.js;

server {
  location / {
    js_content http.test;
  }
}
```

- `js_import` - [lib:Nginx NJs module] directive that loads specified NJs file into Nginx
- `test.js` - load [NJs code]() file
- `server {` - virtual server configuration block
- `location / {` - default location block
- `js_content` - return content from specified NJs function
- `http.test` - will call `test()` function from 

group: njs


