# How to SCP multiple files?
// plain

You can use the `scp` command to securely copy multiple files from one host to another.

## Example code

```
scp file1.txt file2.txt user@host:/path/to/destination
```

This command will copy both `file1.txt` and `file2.txt` to the `/path/to/destination` directory on the host `user@host`.

You can also use wildcards to copy multiple files at once. For example, the following command will copy all files with the `.txt` extension from the current directory to the `/path/to/destination` directory on the host `user@host`:

```
scp *.txt user@host:/path/to/destination
```

You can also use the `-r` flag to recursively copy entire directories. For example, the following command will copy the `my_dir` directory and all of its contents to the `/path/to/destination` directory on the host `user@host`:

```
scp -r my_dir user@host:/path/to/destination
```

## Helpful links
- [SCP Command Tutorial](https://www.ssh.com/ssh/scp)
- [Linux SCP Command Examples](https://www.cyberciti.biz/faq/linux-unix-scp-command-examples/)

onelinerhub: [How to SCP multiple files?](https://onelinerhub.com/scp/how-to-scp-multiple-files)