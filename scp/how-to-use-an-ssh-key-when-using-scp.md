# How to use an SSH key when using SCP?
// plain

Using an SSH key when using SCP is a secure way to transfer files between two computers. To use an SSH key when using SCP, you need to generate an SSH key pair on the computer you are transferring from and add the public key to the computer you are transferring to.

## Example code

```
# Generate an SSH key pair
ssh-keygen -t rsa

# Copy the public key to the remote computer
scp ~/.ssh/id_rsa.pub user@remote_host:~/.ssh/authorized_keys
```

The code above will generate an SSH key pair and copy the public key to the remote computer.

## Code explanation


1. `ssh-keygen -t rsa`: Generates an SSH key pair with the RSA algorithm.
2. `scp ~/.ssh/id_rsa.pub user@remote_host:~/.ssh/authorized_keys`: Copies the public key to the remote computer.

## Helpful links

- [How to Use SSH Keys with Windows on Azure](https://docs.microsoft.com/en-us/azure/virtual-machines/windows/use-ssh-keys-to-authenticate)
- [How to Use SSH Keys with Linux on Azure](https://docs.microsoft.com/en-us/azure/virtual-machines/linux/use-ssh-keys-to-authenticate)

onelinerhub: [How to use an SSH key when using SCP?](https://onelinerhub.com/scp/how-to-use-an-ssh-key-when-using-scp)