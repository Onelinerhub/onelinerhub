# Convert hex to int

```sql
SELECT toInt32(unhex('313233'))
```

- `unhex(` - converts given HEX to string
- `toInt32(` - converts text to int (32 bytes, but can use any of [available converters](https://clickhouse.com/docs/en/sql-reference/functions/type-conversion-functions/#toint8163264128256))
- `313233` - sample HEX num (which is `123` int)

group: hex

## Example: 
```sql
SELECT toInt32(unhex('313233'))
```
```
┌─toInt32(unhex('313233'))─┐
│                      123 │
└──────────────────────────┘
```

