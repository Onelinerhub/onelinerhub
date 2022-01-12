# Generate UUID

```sql
SELECT generateUUIDv4()
```

- `generateUUIDv4` - will generate [UUID version 4](https://clickhouse.com/docs/en/sql-reference/functions/uuid-functions/#uuid-function-generate) value

group: uuid

## Example: 
```sql
SELECT generateUUIDv4()
```
```
┌─generateUUIDv4()─────────────────────┐
│ 20309783-d2d0-4723-8235-6da80de62ec8 │
└──────────────────────────────────────┘
```

