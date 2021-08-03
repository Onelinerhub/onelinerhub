# Aliases

```sql
SELECT make, model, price AS original_price, ROUND(price*1.13) AS taxed_price FROM car;
```

- price AS original_price - rename column price to original_price
- ROUND(price*1.13) AS taxed_price - multipy then round each result in the result set then name the column of the result set to taxed_price