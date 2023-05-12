# How to list files using SCP?
// plain

SCP (Secure Copy Protocol) is a secure file transfer protocol used to copy files between two computers over a network. It can be used to list files in a remote directory.

## Example code

```
scp -l <username>@<hostname>:<remote_directory>
```

## Output example

```
file1
file2
file3
```

## Code explanation

- `scp`: command to initiate the SCP protocol
- `-l`: flag to list files in a remote directory
- `<username>`: username of the remote host
- `<hostname>`: hostname or IP address of the remote host
- `<remote_directory>`: path to the remote directory

## Helpful links
- [SCP Command Tutorial](https://www.ssh.com/ssh/scp)
- [SCP Man Page](https://linux.die.net/man/1/scp)

onelinerhub: [How to list files using SCP?](https://onelinerhub.com/scp/how-to-list-files-using-scp)