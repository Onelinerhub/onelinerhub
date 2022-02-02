# How to print terminal/console history with timestamps

```bash
HISTTIMEFORMAT="%F %T " && history
```

- `history` - prints entire commands history for current user
- `HISTTIMEFORMAT` - set format for command time to print
- `%F %T` - e.g. 2022-02-02 16:47:53

group: history

## Example: 
```bash
HISTTIMEFORMAT="%F %T " && history
```
```
 2000  2022-02-02 16:47:53 history --help
 2001  2022-02-02 16:49:03 history | tail -n 10
 2002  2022-02-02 16:51:45 history | grep "git"
 2003  2022-02-02 16:52:56 HISTTIMEFORMAT="%F %T " && history

```

