# How to use SCP with a password?
// plain

SCP (Secure Copy Protocol) is a secure way to transfer files between two computers. It can be used with a password to ensure that only authorized users can access the files.

To use SCP with a password, you need to specify the username and password in the command line. For example:

```
scp -P <port> -r <source_file> <username>@<host>:<destination_file>
```

The `-P` option specifies the port to use for the connection, `-r` is used to copy directories recursively, `<source_file>` is the file or directory to be copied, `<username>` is the username of the remote host, `<host>` is the hostname or IP address of the remote host, and `<destination_file>` is the destination file or directory.

When the command is executed, you will be prompted for the password. Enter the password and the files will be copied securely.

## Code explanation

- `-P`: specifies the port to use for the connection
- `-r`: copies directories recursively
- `<source_file>`: file or directory to be copied
- `<username>`: username of the remote host
- `<host>`: hostname or IP address of the remote host
- `<destination_file>`: destination file or directory

## Helpful links
- [SCP Command Tutorial](https://www.ssh.com/ssh/scp)
- [SCP Command Examples](https://www.cyberciti.biz/faq/linux-unix-scp-command-examples/)

onelinerhub: [How to use SCP with a password?](https://onelinerhub.com/scp/how-to-use-scp-with-a-password)