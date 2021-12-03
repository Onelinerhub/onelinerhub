# How to get open ports

```bash
ufw status verbose
```

- `status verbose` - will return list of current rules, including opened/closed ports

## Example: 
```bash
ufw status verbose
```
```
To                         Action      From
--                         ------      ----
80                         DENY IN     Anywhere                  
Anywhere                   ALLOW IN    1.2.3.4                   
80 (v6)                    DENY IN     Anywhere (v6)  
```

## Additional keywords
- list
- retrieve
- fetch
- see
