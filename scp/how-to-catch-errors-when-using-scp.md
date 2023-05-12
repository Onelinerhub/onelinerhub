# How to catch errors when using SCP?
// plain

SCP (Secure Copy Protocol) is a secure way to transfer files between two computers. To catch errors when using SCP, you can use the `-v` flag to enable verbose mode. This will print out detailed information about the progress of the transfer, including any errors that occur.

## Example


```
scp -v file.txt user@host:/path/to/destination
```

## Output example


```
Executing: program /usr/bin/ssh host scp -v -t /path/to/destination
OpenSSH_7.6p1 Ubuntu-4ubuntu0.3, OpenSSL 1.0.2n  7 Dec 2017
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 19: Applying options for *
debug1: Connecting to host [192.168.1.1] port 22.
debug1: Connection established.
debug1: key_load_public: No such file or directory
debug1: identity file /home/user/.ssh/id_rsa type -1
debug1: key_load_public: No such file or directory
debug1: identity file /home/user/.ssh/id_rsa-cert type -1
debug1: key_load_public: No such file or directory
debug1: identity file /home/user/.ssh/id_dsa type -1
debug1: key_load_public: No such file or directory
debug1: identity file /home/user/.ssh/id_dsa-cert type -1
debug1: key_load_public: No such file or directory
debug1: identity file /home/user/.ssh/id_ecdsa type -1
debug1: key_load_public: No such file or directory
debug1: identity file /home/user/.ssh/id_ecdsa-cert type -1
debug1: key_load_public: No such file or directory
debug1: identity file /home/user/.ssh/id_ed25519 type -1
debug1: key_load_public: No such file or directory
debug1: identity file /home/user/.ssh/id_ed25519-cert type -1
debug1: Local version string SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3
debug1: Remote protocol version 2.0, remote software version OpenSSH_7.2p2 Ubuntu-4ubuntu2.8
debug1: match: OpenSSH_7.2p2 Ubuntu-4ubuntu2.8 pat OpenSSH* compat 0x04000000
debug1: Authenticating to host:22 as 'user'
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: algorithm: curve25519-sha256
debug1: kex: host key algorithm: ecdsa-sha2-nistp256
debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: Server host key: ecdsa-sha2-nistp256 SHA256:<key>
debug1: Host 'host' is known and matches the ECDSA host key.
debug1: Found key in /home/user/.ssh/known_hosts:1
debug1: rekey after 134217728 blocks
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: rekey after 134217728 blocks
debug1: SSH2_MSG_EXT_INFO received
debug1: kex_input_ext_info: server-sig-algs=<rsa-sha2-256,rsa-sha2-512>
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug1: Authentications that can continue: publickey,password
debug1: Next authentication method: publickey
debug1: Offering RSA public key: /home/user/.ssh/id_rsa
debug1: Authentications that can continue: publickey,password
debug1: Trying private key: /home/user/.ssh/id_dsa
debug1: Trying private key: /home/user/.ssh/id_ecdsa
debug1: Trying private key: /home/user/.ssh/id_ed25519
debug1: Next authentication method: password
user@host's password:
debug1: Authentication succeeded (password).
Authenticated to host ([192.168.1.1]:22).
debug1: channel 0: new [client-session]
debug1: Requesting no-more-sessions@openssh.com
debug1: Entering interactive session.
debug1: Sending command: scp -v -t /path/to/destination
Sending file.txt
debug1: client_input_channel_req: channel 0 rtype exit-status reply 0
debug1: channel 0: free: client-session, nchannels 1
Transferred: sent 3200, received 2880 bytes, in 0.2 seconds
Bytes per second: sent 16000.0, received 14400.0
debug1: Exit status 0
```

The output will show any errors that occur during the transfer, such as authentication errors, connection errors, or file transfer errors.

## Code explanation


- `scp -v file.txt user@host:/path/to/destination`: This is the command used to transfer the file. The `-v` flag enables verbose mode, which will print out detailed information about the progress of the transfer.

- `debug1: Connection established.`: This line indicates that the connection to the remote host was successfully established.

- `debug1: Exit status 0`: This line indicates that the transfer was successful and no errors occurred.

## Helpful links

- [SCP Command Tutorial](https://www.ssh.com/ssh/scp)
- [SCP Man Page](https://linux.die.net/man/1/scp)

onelinerhub: [How to catch errors when using SCP?](https://onelinerhub.com/scp/how-to-catch-errors-when-using-scp)