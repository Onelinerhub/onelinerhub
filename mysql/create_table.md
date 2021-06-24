# Create table

```sql
CREATE TABLE tbl(id int auto_increment primary key, name varchar(128));
```

- tbl - table name to create
- id int - first column definition, named ```id``` of type ```int```
- auto_increment - automatically set ids based on int counter
- primary key - set first column as primary key (can't have duplicate values)
- name varchar(128) - second column definition, named ```name``` of type ```varchar``` (128 chars limit)
