# Convert array to string

```sql
SELECT arrayStringConcat(['I', 'am', 'string'], ' ')
```

- `arrayStringConcat` - will join all array elements into string using specified separator
- `['I', 'am', 'string']` - sample array to convert to string
- `' '` - separator to user to join array elements

group: array_to

## Example: 
```sql
SELECT arrayStringConcat(['I', 'am', 'string'], ' ')
```
```
┌─arrayStringConcat(['I', 'am', 'string'], ' ')─┐
│ I am string                                   │
└───────────────────────────────────────────────┘
```

link_youtube: https://youtu.be/ODz23YLL53A
