# Running SCP in quiet mode
// plain

SCP (Secure Copy Protocol) is a network protocol used to securely transfer files between two computers. It can be run in quiet mode, which suppresses all output to the terminal.

## Example code

```
scp -q <source> <destination>
```

## Output example

```
No output
```

## Code explanation

- `scp`: the command to run the Secure Copy Protocol
- `-q`: the flag to run SCP in quiet mode
- `<source>`: the file or directory to be copied
- `<destination>`: the location to copy the file or directory to

## Helpful links
- [SCP on Wikipedia](https://en.wikipedia.org/wiki/Secure_copy)
- [SCP man page](https://linux.die.net/man/1/scp)

onelinerhub: [Running SCP in quiet mode](https://onelinerhub.com/scp/running-scp-in-quiet-mode)