# How do I convert a gzip tar file to a tgz file?
// plain

To convert a gzip tar file to a tgz file, you can use the `tar` command in combination with the `gzip` command. The `tar` command is used to create an archive of files, and the `gzip` command is used to compress the archive.

For example, to convert a gzip tar file named `example.tar.gz` to a tgz file named `example.tgz`, you can use the following command:

```
tar -czvf example.tgz example.tar.gz
```

The parts of this command are:

* `tar` - The command to create an archive
* `-czvf` - The flags for the command, which are:
  * `-c` - Create a new archive
  * `-z` - Compress the archive with `gzip`
  * `-v` - Verbosely list files processed
  * `-f` - Use the next argument as the archive file
* `example.tgz` - The name of the resulting tgz file
* `example.tar.gz` - The name of the original gzip tar file

After running this command, the original gzip tar file will be converted to a tgz file.

## Helpful links

* [tar command](https://www.computerhope.com/unix/utar.htm)
* [gzip command](https://www.computerhope.com/unix/ugzip.htm)

onelinerhub: [How do I convert a gzip tar file to a tgz file?](https://onelinerhub.com/cli-tar/how-do-i-convert-a-gzip-tar-file-to-a-tgz-file)