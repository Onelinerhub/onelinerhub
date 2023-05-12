# How to SCP all files in a directory?
// plain

To SCP all files in a directory, you can use the `scp` command.

## Example code

```
scp -r <source_directory> <username>@<hostname>:<destination_directory>
```

This command will copy all files and subdirectories from the `<source_directory>` to the `<destination_directory>` on the remote host. The `-r` flag is used to indicate that the source directory should be copied recursively.

## Code explanation

- `scp`: the command used to copy files over a network
- `-r`: the flag used to indicate that the source directory should be copied recursively
- `<source_directory>`: the directory on the local machine that should be copied
- `<username>@<hostname>`: the username and hostname of the remote machine
- `<destination_directory>`: the directory on the remote machine where the files should be copied

## Helpful links
- [SCP Command Tutorial](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)

onelinerhub: [How to SCP all files in a directory?](https://onelinerhub.com/scp/how-to-scp-all-files-in-a-directory)