# How to get 95% percentile

```sql
SELECT quantile(0.95)(age) FROM tbl;
```

- `quantile(0.95)` - will return 95% percentile value for specified column
- `age` - name of the column to get percentile value for

group: percentiles


