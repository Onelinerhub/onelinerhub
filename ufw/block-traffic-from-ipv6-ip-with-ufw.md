# Block traffic from IPV6 IP with ufw

```bash
ufw deny proto ipv6 from x:x:x:x:x:x:x:x
```

- `deny` - deny traffic by specified rule
- `proto ipv6` - IPV6 protocol
- `from x:x:x:x:x:x:x:x` - IPV6 address to block traffic from

group: ipv6


## Additional keywords
- disable
- deny
- restrict
