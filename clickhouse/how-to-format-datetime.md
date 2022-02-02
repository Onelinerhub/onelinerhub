# How to format date/time

```sql
SELECT formatDateTime(now(), '%Y, %d/%m %H:%M (:%S)')
```

- `now()` - returns current date/time
- `formatDateTime` - formats given date/time with a specified pattern
- `%Y` - year
- `%d` - day
- `%m` - month
- `%H` - hours
- `%M` - minutes
- `%S` - seconds

group: date_format

## Example: 
```sql
SELECT formatDateTime(now(), '%Y, %d/%m %H:%M (:%S)')
```
```
┌─formatDateTime(now(), '%Y, %d/%m %H:%M (:%S)')─┐
│ 2022, 12/01 17:20 (:45)                        │
└────────────────────────────────────────────────┘

```

link_youtube: https://youtu.be/ULndndtqBus
