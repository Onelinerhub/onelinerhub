# How to download a file using SCP?
// plain

SCP (Secure Copy Protocol) is a secure way to transfer files between two computers. To download a file using SCP, you need to have the following:

1. A source computer with the file you want to download
2. A destination computer to download the file to

To download a file using SCP, you can use the following command:

```
scp username@source_host:/path/to/file /destination/path
```

This command will copy the file from the source computer to the destination computer.

## Code explanation


1. `scp` - The command to initiate the SCP transfer
2. `username@source_host` - The username and hostname of the source computer
3. `/path/to/file` - The path to the file on the source computer
4. `/destination/path` - The path to the destination directory on the destination computer

## Helpful links

- [SCP Command Tutorial](https://www.ssh.com/ssh/scp)
- [SCP Examples](https://www.cyberciti.biz/faq/linux-unix-scp-command-examples/)

onelinerhub: [How to download a file using SCP?](https://onelinerhub.com/scp/how-to-download-a-file-using-scp)