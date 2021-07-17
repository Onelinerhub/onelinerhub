# Rename table column

```sql
ALTER TABLE tbl CHANGE col col_new type;
```

- tbl - table to rename column of
- col - old column name
- col_new - new column name
- type - type of new column

group: rename

other_way: mysql 8.0+ & mariadb 10.5.2+

```sql
ALTER TABLE tbl RENAME COLUMN col TO col_new;
```

- tbl - table to rename column of
- col - old column name
- col_new - new column name
