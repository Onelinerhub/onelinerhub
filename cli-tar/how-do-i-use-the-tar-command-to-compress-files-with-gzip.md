# How do I use the tar command to compress files with gzip?
// plain

The `tar` command is used to create, modify, and extract files from an archive. It is often used in conjunction with a compression utility, such as `gzip`, to compress files for storage or transport.

To compress files with `gzip`, the `-z` or `--gzip` option can be used with the `tar` command.

For example, to compress a directory of files into a single `.tar.gz` archive file, use the following command:
```
tar -czvf archive.tar.gz /path/to/directory
```

The command above will create a file named `archive.tar.gz` containing all files and directories in the specified directory.

The flags used in the command are:
- `-c` to create an archive
- `-z` to compress the archive with `gzip`
- `-v` to be verbose and show the progress
- `-f` to specify the output file

For more information about the `tar` command, see the [GNU tar manual](https://www.gnu.org/software/tar/manual/tar.html).

onelinerhub: [How do I use the tar command to compress files with gzip?](https://onelinerhub.com/cli-tar/how-do-i-use-the-tar-command-to-compress-files-with-gzip)