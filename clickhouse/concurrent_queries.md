# Increase number of concurrent queries

### Settings should be edited in `/etc/clickhouse-server/config.xml` file:

```xml
<max_concurrent_queries>500</max_concurrent_queries>
```

- `max_concurrent_queries` - this setting limits number of queries executing concurrently


