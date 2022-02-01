# Format date in "YYYYMMDD"

```sql
SELECT toYYYYMMDD(now())
```

- `now()` - returns current date/time
- `toYYYYMMDD` - format given date/time in "YYYYMMDD" style

group: date_format

## Example: 
```sql
SELECT toYYYYMMDD(now())
```
```
┌─toYYYYMMDD(now())─┐
│          20220112 │
└───────────────────┘
```

link_youtube: https://youtu.be/jBTag2Att-I
