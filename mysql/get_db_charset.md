# Get default charset of a database

```sql
SELECT DEFAULT_CHARACTER_SET_NAME FROM information_schema.SCHEMATA WHERE schema_name = 'db';
```

- DEFAULT_CHARACTER_SET_NAME - will select dafault charset for specified databse
- information_schema.SCHEMATA - system table with meta information for databases
- 'db' - name of our databse to get charset for

group: get_charset
