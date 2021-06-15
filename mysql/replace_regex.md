# Replace string with regex

```sql
UPDATE table SET column = REGEXP_REPLACE(column, '[0-9]+', 'N');
```

- table - example table name
- column - name of column to update/replace
- REGEXP_REPLACE(column - executes [regular expression replace](https://dev.mysql.com/doc/refman/8.0/en/regexp.html#function_regexp-replace) replace over ```column``` column
- '[0-9]+' - regex pattern to search for
- 'N' - text to replace matched strings to

group: str_replace
