# Check if ufw logs are enabled

```bash
ufw status verbose | grep Logging
```

- `status verbose` - will print detailed status (`ufw` should be [activated](/ufw/how-to-activate-ufw))
- `grep Logging` - filter only logging part

group: log

## Example: 
```bash
ufw status verbose | grep Logging
```
```
Logging: on (medium)
```
