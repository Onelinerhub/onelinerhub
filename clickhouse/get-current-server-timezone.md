# Get current server timezone

```sql
SELECT timezone()
```

- `timezone` - will return current Clickhouse server timezone

group: timezone

## Example: 
```sql
SELECT timezone()
```
```
┌─timezone()────┐
│ Europe/Lisbon │
└───────────────┘
```

link_youtube: https://youtu.be/1qIqrE1Ovdk
