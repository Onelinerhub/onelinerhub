# And & Or

```sql
SELECT * FROM person WHERE gender = 'FEMALE' AND (country_of_birth = 'CA' OR country_of_birth = 'US');
```

- SELECT * FROM person - select all columns from table person
- WHERE - filter the results by a condition
- gender = 'FEMALE' - condition1 
- country_of_birth = 'CA' - condition2
- country_of_birth = 'US' - condition3
- AND - tests both condition1 and condition2
- OR - tests both (condition1 and condition2) or condition3