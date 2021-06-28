# Case insensitive search on text column

```sql
SELECT * FROM tbl WHERE lowerUTF8(text) LIKE '%search%';
```

- tbl - name of the table to search in
- text - name of the text column to search on
- lowerUTF8( - will lower-case column values
- '%search%' - substring to search for
