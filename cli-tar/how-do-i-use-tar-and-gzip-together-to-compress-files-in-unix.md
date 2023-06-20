# How do I use tar and gzip together to compress files in Unix?
// plain

The tar command is used to create an archive of multiple files and the gzip command is used to compress the archive. To compress files using tar and gzip together in Unix, use the following command:

```
tar -zcvf <archive_name>.tar.gz <file1> <file2> <file3>
```

This command will create an archive of the files specified, compress the archive using gzip, and save it with the name specified.

Parts of the command:
- `tar`: command to create an archive of multiple files
- `-zcvf`: flags to compress the archive using gzip and save it with a specified name
- `<archive_name>.tar.gz`: name of the compressed archive
- `<file1> <file2> <file3>`: names of the files to compress

For more information on the tar command, see the [GNU Tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_45.html).

onelinerhub: [How do I use tar and gzip together to compress files in Unix?](https://onelinerhub.com/cli-tar/how-do-i-use-tar-and-gzip-together-to-compress-files-in-unix)