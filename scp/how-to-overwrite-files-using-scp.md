# How to overwrite files using SCP?
// plain

SCP (Secure Copy Protocol) is a secure way to transfer files between two computers. To overwrite files using SCP, you can use the `-o` flag. This flag will overwrite existing files with the same name.

## Example

```
scp -o <source_file> <username>@<hostname>:<destination_file>
```

This command will copy the `source_file` to the `destination_file` on the remote host, overwriting any existing file with the same name.

## Code explanation

- `-o`: Flag to overwrite existing files with the same name
- `<source_file>`: Path to the file to be copied
- `<username>`: Username of the remote host
- `<hostname>`: Hostname of the remote host
- `<destination_file>`: Path to the destination file on the remote host

## Helpful links
- [SCP Command Tutorial](https://www.ssh.com/ssh/scp)

onelinerhub: [How to overwrite files using SCP?](https://onelinerhub.com/scp/how-to-overwrite-files-using-scp)