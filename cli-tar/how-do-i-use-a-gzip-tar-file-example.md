# How do I use a gzip tar file example?
// plain

A gzip tar file is an archive file that contains multiple files in a compressed format. To use a gzip tar file, you must first extract the files from the archive. This can be done with the tar command.

For example, to extract the files from a gzip tar file named `example.tgz`, you can use the following command:
```
tar -xzf example.tgz
```
The `-x` flag tells the command to extract the files, the `-z` flag tells the command to use gzip compression, and the `-f` flag tells the command the filename of the archive.

The command will extract the files from the archive into the current directory.

The parts of the command are:
- `tar`: The tar command is used to extract files from an archive.
- `-x`: This flag tells the command to extract the files.
- `-z`: This flag tells the command to use gzip compression.
- `-f`: This flag tells the command the filename of the archive.
- `example.tgz`: This is the name of the gzip tar file.

For more information about the tar command, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html).

onelinerhub: [How do I use a gzip tar file example?](https://onelinerhub.com/cli-tar/how-do-i-use-a-gzip-tar-file-example)