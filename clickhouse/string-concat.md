# String concat

```sql
SELECT concat('Hi', ' ', 'all', '!')
```

- `concat` - will concatenate all given strings into single string
- `'Hi', ' ', 'all', '!'` - strings to join

group: strings

## Example: 
```sql
SELECT concat('Hi', ' ', 'all', '!')
```
```
┌─concat('Hi', ' ', 'all', '!')─┐
│ Hi all!                       │
└───────────────────────────────┘
```

