# How do I extract files from a tar archive using the command line?
// plain

To extract files from a tar archive using the command line, you can use the `tar` command.

```
tar -xvf <filename>.tar
```

This command will extract all files from the tar archive. The flags used are:
- `-x`: extract files from an archive
- `-v`: verbosely list files processed
- `-f`: use archive file or device

The output of this command will be a list of all the files extracted from the tar archive.

You can also extract specific files from the tar archive using the `tar` command.

```
tar -xvf <filename>.tar <file1> <file2> ...
```

This command will extract the specified files from the tar archive.

You can also extract files to a specific directory using the `tar` command.

```
tar -xvf <filename>.tar -C <directory>
```

This command will extract all files from the tar archive to the specified directory.

For more information about the `tar` command, you can refer to the [GNU Tar Manual](https://www.gnu.org/software/tar/manual/tar.html).

onelinerhub: [How do I extract files from a tar archive using the command line?](https://onelinerhub.com/cli-tar/how-do-i-extract-files-from-a-tar-archive-using-the-command-line)