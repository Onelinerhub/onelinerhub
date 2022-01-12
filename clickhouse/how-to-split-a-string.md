# How to split a string

```sql
SELECT splitByString(' ', 'Hello all of you')
```

- `splitByString` - will split given string (second argument) by a specified substring (first argument)
- `' '` - string to split by (space)
- `'Hello all of you'` - sample string to split

group: strings

## Example: 
```sql
SELECT splitByString(' ', 'Hello all of you')
```
```
┌─splitByString(' ', 'Hello all of you')─┐
│ ['Hello','all','of','you']             │
└────────────────────────────────────────┘
```

