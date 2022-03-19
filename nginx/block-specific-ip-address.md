# Block specific IP address

```nginx
server {
  deny 1.2.3.4;
}
```

- `server {` - virtual server configuration block
- `deny` - deny access to the specified IP
- `1.2.3.4` - IP to block access for

group: block


