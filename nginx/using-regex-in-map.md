# Using regex in map

```nginx
map $request_uri $private_req {
  default 0;
  "~*\/admin.*" 1;
  "~*\/manage.*" 1;
}

server {
  if ( $private_req ) {
    return 403 'No russians, sorry';
  }
}
```

- `map` - define variables map
- `$request_uri` - variable to match patterns agains
- `$private_req` - variable to fill with resulting values
- `default 0` - default value for mapped variable
- `~*\/admin.*` - sample regex to match (string matches `/admin...` text)
- `~*\/manage.*` - other sample regex to match (string matches `/manage...` text)
- `server {` - virtual server configuration block
- `if ( $private_req ) {` - will be triggered when `$private_req` contains `1`
- `return 403 'No russians, sorry';` - return `403` status code

group: map


