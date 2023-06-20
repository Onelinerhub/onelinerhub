# How do I use gzip or tar to compress a file?
// plain

Using gzip or tar to compress a file is a simple process.

To compress a file using gzip, use the following command:

```
gzip <filename>
```

This will create a new file with the same name but with the extension `.gz`. The original file will remain unchanged.

To compress a file using tar, use the following command:

```
tar -zcvf <filename>.tar.gz <filename>
```

This will create a new file with the extension `.tar.gz`. The original file will remain unchanged.

## Code explanation

- `gzip`: command to compress a file using gzip
- `<filename>`: name of the file to be compressed
- `tar`: command to compress a file using tar
- `-zcvf`: flags used with tar to compress the file
- `.tar.gz`: extension of the compressed file

## Helpful links
- [GZIP](https://www.computerhope.com/unix/ugzip.htm)
- [TAR](https://www.computerhope.com/unix/utar.htm)

onelinerhub: [How do I use gzip or tar to compress a file?](https://onelinerhub.com/cli-tar/how-do-i-use-gzip-or-tar-to-compress-a-file)