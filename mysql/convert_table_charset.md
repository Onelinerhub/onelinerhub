# Convert table charset to UTF8

```sql
ALTER TABLE table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

- table - table name to change charset of
- utf8mb4 - utf8 encoding (charset)
- utf8mb4_unicode_ci - utf8 collation (strings comparison rules)

group: convert_charset
