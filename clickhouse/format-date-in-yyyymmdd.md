# Format date in "YYYYMMDD"

```sql
SELECT toYYYYMMDD(now())
```

- `now()` - returns current date/time
- `toYYYYMMDD` - format given date/time in "YYYYMMDD" style

## Example: 
```sql
SELECT toYYYYMMDD(now())
```
```
┌─toYYYYMMDD(now())─┐
│          20220112 │
└───────────────────┘
```

