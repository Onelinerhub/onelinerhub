# Deny connections from subnet

```ufw
ufw deny from 1.2.3.0/24
```

- `from 1.2.3.0/24` - specify subnet to allow connections from
- `deny` - denies all connections from specified subnet

group: subnet


## Additional keywords
- block
- restrict
- close
- forbid
