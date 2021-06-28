# Insert string array in CSV format

```sql
INSERT INTO tbl FORMAT CSV 10, "['str1', 'str2']"
```

- tbl - name of the table to insert data to (assume it has 2 columns: ```a Int32, b Array(String)```)
- FORMAT CSV - specify format for date insert
- 10 - value of ```a``` column
- "\['str1', 'str2'\]" - value of ```b``` column, array of strings
