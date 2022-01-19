# Change memory limit

### You should edit this configuration option in `/etc/clickhouse-server/users.xml` (for `default` or specific user profile):

```xml
 <max_memory_usage>8000000000</max_memory_usage>
```

- `max_memory_usage` - will set max memory usage when executing queries
- `8000000000` - set to `8G`


