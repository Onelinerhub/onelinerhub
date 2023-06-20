# How do I compress a file using gzip and tar.xz?
// plain

To compress a file using gzip and tar.xz, you can use the following command:

```
tar -cvJf <file_name>.tar.xz <file_name>
```

This command will create a tar archive file named `<file_name>.tar.xz` which is compressed with xz.

You can also compress the file with gzip, using the following command:

```
tar -cvzf <file_name>.tar.gz <file_name>
```

This command will create a tar archive file named `<file_name>.tar.gz` which is compressed with gzip.

You can also combine these two commands, to compress the file using both gzip and xz, using the following command:

```
tar -cvJf <file_name>.tar.xz -cvzf <file_name>.tar.gz <file_name>
```

This command will create two tar archive files, `<file_name>.tar.xz` and `<file_name>.tar.gz`, which are compressed with xz and gzip respectively.

## Helpful links
- [Gzip Compression](https://www.thegeekstuff.com/2012/04/gzip-commands/)
- [Tar and XZ Compression](https://www.thegeekstuff.com/2015/03/tar-xz-file/)

onelinerhub: [How do I compress a file using gzip and tar.xz?](https://onelinerhub.com/cli-tar/how-do-i-compress-a-file-using-gzip-and-tar-xz)