# Get year and month from date

```sql
SELECT toYYYYMM(now())
```

- `now()` - returns current date/time
- `toYYYYMM` - extracts year and month from given date/time

group: date_format

## Example: 
```sql
SELECT toYYYYMM(now())
```
```
┌─toYYYYMM(now())─┐
│          202201 │
└─────────────────┘
```

