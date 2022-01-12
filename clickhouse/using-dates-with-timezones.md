# Using dates with timezones

```sql
SELECT toDateTime(now(), 'Europe/Lisbon')
```

- `now()` - returns current date/time
- `toDateTime` - converts given string to DateTime
- `Europe/Lisbon` - pass timezone to convert date/time to as a second argument

## Example: 
```sql
SELECT toDateTime(now(), 'Europe/Lisbon')
```
```
┌─toDateTime(now(), 'Europe/Lisbon')─┐
│                2022-01-12 15:29:48 │
└────────────────────────────────────┘
```

