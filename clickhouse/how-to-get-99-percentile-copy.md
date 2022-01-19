# How to get 99% percentile COPY

```sql
SELECT quantile(0.99)(age) FROM tbl;
```

- `quantile(0.99)` - will return 99% percentile value for specified column
- `age` - name of the column to get percentile value for

group: percentiles


