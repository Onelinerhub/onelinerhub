# How to use aliases

```sql
SELECT make, model, price AS original_price, ROUND(price*1.13) AS taxed_price FROM car;
```

- price AS original_price - rename column `price` to `original_price` in the resulting set
- ROUND(price*1.13) AS taxed_price - multipy then round each value in the result set, then name this column in the resulting table as `taxed_price`
