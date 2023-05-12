# How to SCP from a remote to a local machine?
// plain

SCP (Secure Copy Protocol) is a secure way to transfer files between two computers. To SCP from a remote to a local machine, you need to use the `scp` command in the terminal.

## Example

```
scp username@remotehost.edu:/path/to/file /local/destination
```

This command will copy the file located at `/path/to/file` on the remote host `remotehost.edu` to the local destination `/local/destination` using the username `username`.

## Code explanation

- `scp`: the command to initiate the secure copy
- `username@remotehost.edu`: the username and hostname of the remote machine
- `/path/to/file`: the path to the file on the remote machine
- `/local/destination`: the local destination to copy the file to

## Helpful links
- [SCP Command Tutorial](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)

onelinerhub: [How to SCP from a remote to a local machine?](https://onelinerhub.com/scp/how-to-scp-from-a-remote-to-a-local-machine)