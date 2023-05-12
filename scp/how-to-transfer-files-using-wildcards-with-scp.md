# How to transfer files using wildcards with SCP?
// plain

Wildcards can be used to transfer multiple files with SCP. The syntax for using wildcards is `scp <source> <destination>`.

## Example

```
scp /home/user/files/*.txt user@example.com:/home/user/
```
This command will transfer all files with the .txt extension from the `/home/user/files/` directory to the `/home/user/` directory on the remote server.

## Code explanation

- `scp`: The command to initiate the file transfer
- `/home/user/files/*.txt`: The source directory and wildcard for the files to be transferred
- `user@example.com:/home/user/`: The destination directory on the remote server

## Helpful links
- [SCP Command Tutorial](https://www.ssh.com/ssh/scp)
- [Wildcards in SCP](https://www.ssh.com/ssh/scp/wildcards)

onelinerhub: [How to transfer files using wildcards with SCP?](https://onelinerhub.com/scp/how-to-transfer-files-using-wildcards-with-scp)