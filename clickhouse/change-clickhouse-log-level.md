# Change Clickhouse log level

### In order to change Clickhouse log level (`trace` by default), change this setting in `/etc/clickhouse-server/config.xml`:

```xml
<level>error</level>
```

- `level` - set logging level
- `error` - log only errors

group: logs


