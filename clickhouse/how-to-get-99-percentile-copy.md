# How to get 99% percentile

```sql
SELECT quantile(0.99)(age) FROM tbl;
```

- `quantile(0.99)` - will return 99% percentile value for specified column
- `age` - name of the column to get percentile value for

group: percentiles


link_youtube: https://youtu.be/gkHcxQ6wo9g
