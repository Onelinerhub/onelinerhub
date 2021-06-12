# How to duplicate table structure and data

```sql
CREATE TABLE new LIKE old;
INSERT INTO new SELECT * FROM old;
```

- CREATE TABLE new - create new table named ```new``` 
- LIKE old - our ```new``` table will have the same structure as ```old``` (our current table)
- INSERT INTO new SELECT * FROM old - will copy all the data from ```old``` to ```new```
