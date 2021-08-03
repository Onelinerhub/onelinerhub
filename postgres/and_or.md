# And & Or

```sql
SELECT * FROM person WHERE gender = 'Female' AND (country_of_birth = 'CA' OR country_of_birth = 'US');
```

- SELECT * FROM person - select all columns from table `person`
- WHERE - filter the results by a condition
- gender = 'FEMALE' - first condition
- country_of_birth = 'CA' - second condition
- country_of_birth = 'US' - third condition
- AND - tests both first and second conditions
- OR - tests both (first and second conditions) or third condition
