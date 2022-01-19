# Array zip example

```sql
SELECT arrayZip([1, 2], ['Donald', 'Joe'])
```

- `arrayZip` - will join 2 arrays into array of tuples of corresponding values
- `[1, 2]` - first array
- `['Donald', 'Joe']` - second array

## Example: 
```sql
SELECT arrayZip([1, 2], ['Donald', 'Joe'])
```
```
┌─arrayZip([1, 2], ['Donald', 'Joe'])─┐
│ [(1,'Donald'),(2,'Joe')]            │
└─────────────────────────────────────┘
```

link_youtube: https://youtu.be/bgK9yGreQdU
