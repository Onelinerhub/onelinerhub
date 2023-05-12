# How to automatically create destination directory when using SCP?
// plain

SCP (Secure Copy Protocol) is a secure file transfer protocol used to copy files between two remote hosts. It is possible to automatically create a destination directory when using SCP by using the `-T` flag.

## Example code

```
scp -T /path/to/source/file user@host:/path/to/destination/
```

## Output example

```
/path/to/destination/ created
```

## Code explanation

- `scp`: the command to initiate the SCP protocol
- `-T`: the flag to create the destination directory if it does not exist
- `/path/to/source/file`: the path to the source file
- `user@host`: the user and host of the destination
- `/path/to/destination/`: the path to the destination directory

## Helpful links
- [SCP Command Tutorial](https://www.ssh.com/ssh/scp)

onelinerhub: [How to automatically create destination directory when using SCP?](https://onelinerhub.com/scp/how-to-automatically-create-destination-directory-when-using-scp)