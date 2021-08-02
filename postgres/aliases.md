# Aliases

```sql
SELECT make, model, price AS original_price, ROUND(price*1.13) AS taxed_price  FROM car;
```

- price AS original_price - name column price to original_price
- ROUND(price*1.13)  - multipy then round each result in the result set
- ROUND(price*1.13) AS taxed_price - name the column of the result set to taxed_price