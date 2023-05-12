# How to run SCP in verbose mode?
// plain

To run SCP in verbose mode, use the `-v` flag. For example:

```
scp -v <source> <destination>
```

This will output the progress of the file transfer, including the amount of data transferred, the speed of the transfer, and the estimated time remaining.

The `-v` flag can be combined with other flags, such as `-r` for recursive transfer, `-P` for port number, and `-C` for compression.

Parts of the code:
- `-v`: flag to enable verbose mode
- `<source>`: the file or directory to be transferred
- `<destination>`: the location to which the file or directory will be transferred

## Helpful links
- [SCP Command Tutorial](https://www.ssh.com/ssh/scp)

onelinerhub: [How to run SCP in verbose mode?](https://onelinerhub.com/scp/how-to-run-scp-in-verbose-mode)