# How do I use a password to compress files with Unix tar?
// plain

To compress files with Unix tar using a password, you need to use the `-z` and `-P` options. `-z` is used to compress the files with gzip, and `-P` is used to specify the password. For example:

```
tar -zcvf -P secret archive.tar.gz file1 file2
```

The above command will compress `file1` and `file2` into `archive.tar.gz` with password `secret`.

The parts of the code are as follows:

- `tar`: The command for compressing files with Unix tar
- `-z`: The option to compress the files with gzip
- `-P`: The option to specify the password
- `secret`: The password to be used
- `archive.tar.gz`: The name of the compressed file
- `file1` and `file2`: The files to be compressed

## Helpful links

- [Unix tar command](https://www.computerhope.com/unix/utar.htm)
- [Using tar command with gzip compression](https://www.cyberciti.biz/faq/howto-linux-unix-compress-a-tar-file-with-gzip/)

onelinerhub: [How do I use a password to compress files with Unix tar?](https://onelinerhub.com/cli-tar/how-do-i-use-a-password-to-compress-files-with-unix-tar)