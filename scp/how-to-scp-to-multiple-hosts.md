# How to SCP to multiple hosts?
// plain

SCP (Secure Copy Protocol) is a secure way to transfer files between two hosts. To SCP to multiple hosts, you can use a bash script with a for loop.

```
#!/bin/bash

for host in host1 host2 host3
do
  scp file.txt user@$host:/home/user/
done
```

This will copy the file.txt to the /home/user/ directory of each host.

Parts of the code:
- `#!/bin/bash` - This is the shebang line which tells the system which interpreter to use.
- `for host in host1 host2 host3` - This is the for loop which will iterate over the list of hosts.
- `scp file.txt user@$host:/home/user/` - This is the scp command which will copy the file.txt to the /home/user/ directory of each host.

## Helpful links
- [SCP Command Tutorial](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)
- [Bash For Loop Tutorial](https://linuxize.com/post/bash-for-loop/)

onelinerhub: [How to SCP to multiple hosts?](https://onelinerhub.com/scp/how-to-scp-to-multiple-hosts)