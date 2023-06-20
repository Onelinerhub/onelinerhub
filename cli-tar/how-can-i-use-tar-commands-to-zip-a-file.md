# How can I use tar commands to zip a file?
// plain

The tar command is a useful tool for zipping and unzipping files. It can be used to compress a single file or multiple files into a single archive. To zip a file with the tar command, use the following syntax:

```
tar -zcvf <archive_name.tar.gz> <file_name>
```

This command creates a compressed archive file, named `archive_name.tar.gz`, containing the file `file_name`.

The flags used in the command are:

- `-z`: Compress the archive using gzip.
- `-c`: Create a new archive.
- `-v`: Verbosely list files which are processed.
- `-f`: Use the archive file specified by the given name.

For example, to compress the file `example.txt` into an archive named `example.tar.gz`, use the following command:

```
tar -zcvf example.tar.gz example.txt
```

This will create the archive `example.tar.gz` containing the file `example.txt`.

For more information about the tar command, see the [GNU Tar Manual](https://www.gnu.org/software/tar/manual/html_node/tar_toc.html).

onelinerhub: [How can I use tar commands to zip a file?](https://onelinerhub.com/cli-tar/how-can-i-use-tar-commands-to-zip-a-file)