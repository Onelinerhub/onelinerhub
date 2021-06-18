# Truncate all tables in a specific database

```bash
mysql db -Nse 'show tables' | while read table; do mysql db -e "truncate table $table"; done
```

- mysql db -Nse 'show tables' - prints all tables from ```db``` database line by line
- while read table - execute loop for each table (each line) printed
- mysql db -e "truncate table $table" - execute truncate query for each ```$table``` variable value (each line from previous command)
