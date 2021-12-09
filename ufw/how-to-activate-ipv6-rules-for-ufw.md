# How to activate ipv6 rules for ufw

```bash
cat /etc/default/ufw | grep IPV6
```

- `/etc/default/ufw` - ufw config file
- `grep IPV6` - filter IPV6 settings only

group: ipv6

## Example: 
```bash
cat /etc/default/ufw | grep IPV6
```
```
IPV6=yes
```
