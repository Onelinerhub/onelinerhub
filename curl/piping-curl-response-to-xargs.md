# Piping curl response to xargs

```bash
curl -s https://examples.onelinerhub.com/cmd.sh | xargs ls
```

- `curl` - base curl command
- `-s` - will not display any system information
- `/cmd.sh` - sample URL with text content
- `| ` - pipe downloaded content directly to the specified command
- `xargs` - commands and arguments manipulation utility
- `ls` - will try to list file named exactly as it is in `cmd.sh` file


