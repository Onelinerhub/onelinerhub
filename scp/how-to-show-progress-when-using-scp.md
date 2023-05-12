# How to show progress when using SCP?
// plain

SCP (Secure Copy Protocol) is a secure file transfer protocol used to transfer files between two computers over a network. It can be used to show progress when transferring files by using the `-v` (verbose) flag. This flag will display the progress of the transfer in the terminal.

## Example code

```
scp -v <source_file> <destination_file>
```

## Output example

```
sending incremental file list
./
file1
file2

sent 8 bytes  received 12 bytes  20.00 bytes/sec
total size is 8  speedup is 0.60
```

The `-v` flag will display the following information:

- The list of files being transferred
- The number of bytes sent and received
- The total size of the files being transferred
- The speed of the transfer

## Helpful links
- [SCP Command Tutorial](https://www.ssh.com/ssh/scp)

onelinerhub: [How to show progress when using SCP?](https://onelinerhub.com/scp/how-to-show-progress-when-using-scp)