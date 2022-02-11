# How to replace substrings

```sql
SELECT replaceAll('Thos os odeal', 'o', 'i')
```

- `replaceAll` - replaces all found substrings to new one
- `'Thos os odeal'` - string to search and replace in
- `'o'` - match this substring
- `'i'` - replace to this substring

group: strings

## Example: 
```sql
SELECT replaceAll('Thos os odeal', 'o', 'i')
```
```
┌─replaceAll('Thos os odeal', 'o', 'i')─┐
│ This is ideal                         │
└───────────────────────────────────────┘

```

link_youtube: https://youtu.be/kTdtUMj9mP0
