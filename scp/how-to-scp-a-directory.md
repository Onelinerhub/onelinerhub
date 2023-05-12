# How to SCP a directory?
// plain

SCP (Secure Copy Protocol) is a secure way to transfer files between two computers. To SCP a directory, you can use the following command:
```
scp -r <source_directory> <username>@<hostname>:<destination_directory>
```

This command will copy the `<source_directory>` to the `<destination_directory>` on the remote host `<hostname>` as the user `<username>`.

## Code explanation

- `scp`: the command to initiate the SCP process
- `-r`: the flag to indicate that the source is a directory
- `<source_directory>`: the directory to be copied
- `<username>`: the username of the remote host
- `<hostname>`: the hostname of the remote host
- `<destination_directory>`: the directory on the remote host where the source directory will be copied to

## Helpful links
- [SCP Command Tutorial](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)
- [SCP Man Page](https://linux.die.net/man/1/scp)

onelinerhub: [How to SCP a directory?](https://onelinerhub.com/scp/how-to-scp-a-directory)