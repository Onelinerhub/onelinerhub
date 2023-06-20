# How do I use tar, gzip, and SSH together to transfer files?
// plain

Using tar, gzip, and SSH together is a great way to securely transfer files between two computers. Here's an example of how to do it:

```
tar -zcvf file.tar.gz file1 file2
ssh user@hostname
scp file.tar.gz user@hostname:~/
```

1. `tar -zcvf file.tar.gz file1 file2` - This command creates a tar file with the gzip compression format, which includes the files `file1` and `file2`.
2. `ssh user@hostname` - This command establishes an SSH session with the remote host.
3. `scp file.tar.gz user@hostname:~/` - This command securely copies the file `file.tar.gz` to the remote host.

## Helpful links
- [tar command](https://linuxize.com/post/how-to-use-tar-command-in-linux/)
- [gzip command](https://linuxize.com/post/how-to-use-gzip-command-to-compress-files-in-linux/)
- [ssh command](https://linuxize.com/post/how-to-use-ssh-to-connect-to-a-remote-server-in-linux/)
- [scp command](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)

onelinerhub: [How do I use tar, gzip, and SSH together to transfer files?](https://onelinerhub.com/cli-tar/how-do-i-use-tar--gzip--and-ssh-together-to-transfer-files)