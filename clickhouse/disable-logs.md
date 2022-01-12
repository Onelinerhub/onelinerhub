# Disable logs

### In order to disable Clickhouse logs (`trace` by dafault), change this setting in `/etc/clickhouse-server/config.xml`:

```xml
<level>fatal</level>
```

- `level` - set logging level
- `fatal` - log only fatal errors (you can also use `none` to turn of logging)

group: logs


