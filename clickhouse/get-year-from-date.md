# Get year from date

```sql
SELECT toYear(now())
```

- `toYear` - extracts year part from given date/time
- `now()` - returns current date/time

group: date_format

## Example: 
```sql
SELECT toYear(now())
```
```
┌─toYear(now())─┐
│          2022 │
└───────────────┘
```

link_youtube: https://youtu.be/_4r6RMtcNaE
