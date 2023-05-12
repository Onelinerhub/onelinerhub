# How to transfer files recursively using SCP?
// plain

SCP (Secure Copy Protocol) is a secure way to transfer files between two computers. To transfer files recursively using SCP, you can use the following command:

```
scp -r <source_folder> <username>@<hostname>:<destination_folder>
```

This command will recursively copy all files and folders from the `<source_folder>` to the `<destination_folder>` on the remote host.

## Code explanation


- `scp`: The command to initiate the SCP transfer
- `-r`: The flag to indicate recursive transfer
- `<source_folder>`: The path to the folder on the local machine to be transferred
- `<username>`: The username of the remote host
- `<hostname>`: The hostname or IP address of the remote host
- `<destination_folder>`: The path to the folder on the remote host to which the files will be transferred

## Helpful links

- [SCP Command Tutorial](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)
- [SCP Man Page](https://linux.die.net/man/1/scp)

onelinerhub: [How to transfer files recursively using SCP?](https://onelinerhub.com/scp/how-to-transfer-files-recursively-using-scp)