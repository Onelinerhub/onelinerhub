# How to use SCP without a password?
// plain

SCP (Secure Copy Protocol) is a secure way to transfer files between two computers. It can be used without a password by using SSH keys.

To use SCP without a password, you need to generate an SSH key pair on the local computer and copy the public key to the remote computer.

## Example code


```
# Generate an SSH key pair
ssh-keygen -t rsa

# Copy the public key to the remote computer
scp ~/.ssh/id_rsa.pub user@remote_host:~/.ssh/authorized_keys
```

The code above will generate an SSH key pair and copy the public key to the remote computer.

## Code explanation


1. `ssh-keygen -t rsa`: Generates an SSH key pair on the local computer.
2. `scp ~/.ssh/id_rsa.pub user@remote_host:~/.ssh/authorized_keys`: Copies the public key to the remote computer.

## Helpful links

- [How to Use SCP Without a Password](https://www.digitalocean.com/community/tutorials/how-to-use-scp-to-securely-transfer-files-with-a-remote-server)
- [SSH Key Generation](https://www.ssh.com/ssh/keygen/)

onelinerhub: [How to use SCP without a password?](https://onelinerhub.com/scp/how-to-use-scp-without-a-password)