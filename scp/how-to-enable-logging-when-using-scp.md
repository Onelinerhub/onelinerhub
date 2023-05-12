# How to enable logging when using SCP?
// plain

SCP (Secure Copy Protocol) is a secure file transfer protocol used to transfer files between two computers over a network. Logging can be enabled when using SCP by using the `-v` flag. This flag will enable verbose output which will show the progress of the file transfer.

## Example

```
scp -v <source_file> <username>@<hostname>:<destination_file>
```

## Output example

```
Executing: program /usr/bin/ssh host <hostname>, user <username>, command scp -v -t <destination_file>
OpenSSH_7.6p1 Ubuntu-4ubuntu0.3, OpenSSL 1.0.2n  7 Dec 2017
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: /etc/ssh/ssh_config line 19: Applying options for *
debug1: Connecting to <hostname> [<ip_address>] port 22.
debug1: Connection established.
debug1: identity file /home/<username>/.ssh/id_rsa type 0
debug1: key_load_public: No such file or directory
debug1: identity file /home/<username>/.ssh/id_rsa-cert type -1
debug1: key_load_public: No such file or directory
debug1: identity file /home/<username>/.ssh/id_dsa type -1
debug1: key_load_public: No such file or directory
debug1: identity file /home/<username>/.ssh/id_dsa-cert type -1
debug1: key_load_public: No such file or directory
debug1: identity file /home/<username>/.ssh/id_ecdsa type -1
debug1: key_load_public: No such file or directory
debug1: identity file /home/<username>/.ssh/id_ecdsa-cert type -1
debug1: key_load_public: No such file or directory
debug1: identity file /home/<username>/.ssh/id_ed25519 type -1
debug1: key_load_public: No such file or directory
debug1: identity file /home/<username>/.ssh/id_ed25519-cert type -1
debug1: Local version string SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3
debug1: Remote protocol version 2.0, remote software version OpenSSH_7.6p1 Ubuntu-4ubuntu0.3
debug1: match: OpenSSH_7.6p1 Ubuntu-4ubuntu0.3 pat OpenSSH* compat 0x04000000
debug1: Authenticating to <hostname>:22 as '<username>'
debug1: SSH2_MSG_KEXINIT sent
debug1: SSH2_MSG_KEXINIT received
debug1: kex: algorithm: curve25519-sha256
debug1: kex: host key algorithm: ecdsa-sha2-nistp256
debug1: kex: server->client cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: kex: client->server cipher: chacha20-poly1305@openssh.com MAC: <implicit> compression: none
debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
debug1: Server host key: ecdsa-sha2-nistp256 SHA256:<host_key>
debug1: Host '<hostname>' is known and matches the ECDSA host key.
debug1: Found key in /home/<username>/.ssh/known_hosts:1
debug1: rekey after 134217728 blocks
debug1: SSH2_MSG_NEWKEYS sent
debug1: expecting SSH2_MSG_NEWKEYS
debug1: SSH2_MSG_NEWKEYS received
debug1: rekey after 134217728 blocks
debug1: Will attempt key: /home/<username>/.ssh/id_rsa
debug1: Will attempt key: /home/<username>/.ssh/id_dsa
debug1: Will attempt key: /home/<username>/.ssh/id_ecdsa
debug1: Will attempt key: /home/<username>/.ssh/id_ed25519
debug1: SSH2_MSG_EXT_INFO received
debug1: kex_input_ext_info: server-sig-algs=<ssh-ed25519,ssh-rsa,ssh-dss,ecdsa-sha2-nistp256,ecdsa-sha2-nistp384,ecdsa-sha2-nistp521>
debug1: SSH2_MSG_SERVICE_ACCEPT received
debug1: Authentications that can continue: publickey,password
debug1: Next authentication method: publickey
debug1: Offering public key: /home/<username>/.ssh/id_rsa
debug1: Server accepts key: /home/<username>/.ssh/id_rsa
debug1: Authentication succeeded (publickey).
Authenticated to <hostname> ([<ip_address>]:22).
debug1: channel 0: new [client-session]
debug1: Requesting no-more-sessions@openssh.com
debug1: Entering interactive session.
debug1: Sending command: scp -v -t <destination_file>
Sending file modes: C0664 <filesize> <filename>
```

The `-v` flag enables verbose output which will show the progress of the file transfer. This output includes information about the connection, authentication, and the file transfer.

## Helpful links

- [SCP Command Tutorial](https://linuxize.com/post/how-to-use-scp-command-to-securely-transfer-files/)
- [SCP Man Page](https://linux.die.net/man/1/scp)

onelinerhub: [How to enable logging when using SCP?](https://onelinerhub.com/scp/how-to-enable-logging-when-using-scp)