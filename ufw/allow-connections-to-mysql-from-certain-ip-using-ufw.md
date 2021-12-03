# Allow connections to mysql from certain IP using ufw

```ufw
ufw allow from 1.2.3.4 to any port 3306
```

- `allow` - allows connections
- `from 1.2.3.4` - ip address to allow connections from
- `to any port 3306` - mysql port to allow connections to

group: mysql


## Additional keywords
- accept
- enable
- open
