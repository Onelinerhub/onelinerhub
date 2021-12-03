# Block traffic from IP

```ufw
ufw deny from 1.2.3.4 to any
```

- `deny` - denies traffic by specified rule
- `from 1.2.3.4` - specified IP address to deny connections from
- `to any` - deny connections to all ports and interfaces


## Additional keywords
- deny
- close
- forbid
- connections
- reject
