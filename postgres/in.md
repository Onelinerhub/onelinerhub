# How to filter column based on multiple values

```sql
SELECT first_name FROM person IN ('Joey', 'Austin', 'Richard');
```
- SELECT first_name FROM person - select the column `first_name` from the `person` table
- IN ('Joey', 'Austin', 'Richard') - return rows explicitly matching their `first_name` value with `Joey`, `Austin` or `Richard`
