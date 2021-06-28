# Parse string with date/time to DateTime format

```sql
SELECT parseDateTimeBestEffortOrNull('2021-11-11 07:34:25')
```

- parseDateTimeBestEffortOrNull - will return parsed DateTime (or ```null``` on fail)
- '2021-11-11 07:34:25' - example string date/time string
