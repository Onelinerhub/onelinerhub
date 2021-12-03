# Get all ufw rules

```ufw
ufw status numbered
```

- `status` - print status with list of rules
- `numbered` - will assign numbers to rules

group: rules

## Example: 
```ufw
ufw status numbered
```
```
[ 1] 80                         DENY IN     Anywhere                  
[ 2] Anywhere                   ALLOW IN    1.2.3.4                   
[ 3] 80 (v6)                    DENY IN     Anywhere (v6)
```

## Additional keywords
- list
- see
- retrieve
- print
