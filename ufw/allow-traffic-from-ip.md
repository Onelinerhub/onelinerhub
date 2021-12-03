# Allow traffic from IP

```ufw
ufw allow from 1.2.3.4 to any
```

- `allow` - will allow traffic
- `from 1.2.3.4` - specified IP address to allow connections from
- `to any` - allow connections to all ports and interfaces

group: ip

## Example: 
```ufw
ufw allow from 1.2.3.4 to any
```
```
Rule added
```

## Additional keywords
- deny
- close
- forbid
- connections
- reject
- whitelist
