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

