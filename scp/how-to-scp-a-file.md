# How to SCP a file?
// plain

SCP (Secure Copy Protocol) is a secure way to transfer files between two computers. It uses SSH (Secure Shell) to encrypt the data being transferred.

To SCP a file, you need to use the `scp` command in the terminal. The syntax for the command is:

```
scp [options] source_file target_file
```

where `source_file` is the file you want to copy, and `target_file` is the destination where you want to copy the file.

The `options` part of the command can be used to specify the username and hostname of the source and target computers. For example, if you want to copy a file from a computer with username `user1` and hostname `example.com` to a computer with username `user2` and hostname `example2.com`, you can use the following command:

```
scp -l user1 -h example.com source_file user2@example2.com:target_file
```

The `-l` option specifies the username of the source computer, and the `-h` option specifies the hostname of the source computer. The `user2@example2.com` part specifies the username and hostname of the target computer.

## Helpful links

- [SCP Command Tutorial](https://www.ssh.com/ssh/scp/)
- [SCP Command Examples](https://www.cyberciti.biz/faq/linux-unix-scp-command-examples/)

onelinerhub: [How to SCP a file?](https://onelinerhub.com/scp/how-to-scp-a-file)