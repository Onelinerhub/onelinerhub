# Disable 443 port in ufw

```bash
ufw deny 80
```

- `deny` - blocks connections to specified port
- `443` - HTTPS port

group: 443

## Example: 
```bash
ufw allow 443
```
```
Rule added

```

## Additional keywords
- HTTPS
- block
- deny
- forbid
- reject
