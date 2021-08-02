# In

```sql
SELECT first_name FROM person IN ('Joey', 'Austin', 'Richard');
```
- \\* - refers to every column in table person
- COUNT(*) - aggregate function that returns the number of rows
- IN ('Joey', 'Austin', 'Richard') - return rows explicitly matching first_name with Joey, Austin, and Richard