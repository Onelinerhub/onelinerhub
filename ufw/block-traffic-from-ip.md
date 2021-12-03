# Block traffic from IP

```ufw
ufw reject from 1.2.3.4 to any
```

- `reject` - will reject connections
- `from 1.2.3.4` - specified IP address to reject connections from
- `to any` - reject connections to all ports and interfaces

group: ip


## Additional keywords
- deny
- close
- forbid
- connections
- reject
