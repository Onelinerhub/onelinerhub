# Convert string to date/time

```sql
SELECT toDateTime('2025-05-15 01:02:03')
```

- `toDateTime` - converts given string to date/time
- `2025-05-15 01:02:03` - sample textual date/time

group: date_convert

## Example: 
```sql
SELECT toDateTime('2025-05-15 01:02:03')
```
```
┌─toDateTime('2025-05-15 01:02:03')─┐
│               2025-05-15 01:02:03 │
└───────────────────────────────────┘
```

