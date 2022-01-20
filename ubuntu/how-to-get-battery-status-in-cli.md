# How to get battery status in CLI

```bash
upower -i $(upower -e | grep 'BAT') | grep -E "state|to\ full|percentage"
```

- `upower` - utility to show info on power devices
- `-i` - shows detailed info on specified power source
- `upower -e | grep 'BAT'` - will fetch battery power source name (if any)
- `grep` - show only battery state and percentage


