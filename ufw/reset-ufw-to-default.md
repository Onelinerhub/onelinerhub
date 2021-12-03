# Reset ufw to default

```ufw
ufw --force disable
ufw --force reset
ufw default deny incoming
ufw default allow outgoing
```

- `--force disable` - disable firewall if it's running
- `--force reset` - remove all rules
- `default deny incoming` - block all incoming traffic by default
- `default allow outgoing` - allow all outgoing traffic by default

