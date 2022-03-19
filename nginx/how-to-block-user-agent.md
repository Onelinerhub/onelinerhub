# How to block user agent

```nginx
server {
  if ($http_user_agent ~* wget|bot|curl) {
    return 403;
  }
}
```

- `server {` - virtual server configuration block
- `$http_user_agent` - variable with client user agent
- `wget|bot|curl` - sample regex to filter user agents
- `return 403;` - deny access if user agent matches specified regex

group: block


