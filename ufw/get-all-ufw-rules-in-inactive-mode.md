# Get all ufw rules in inactive mode

```bash
ufw show added
```

- `show added` - will print all added rules even in inactive mode

group: rules

## Example: 
```bash
ufw show added
```
```
ufw deny 80
ufw allow from 1.2.3.4
```

## Additional keywords
- list
- see
- retrieve
- print
