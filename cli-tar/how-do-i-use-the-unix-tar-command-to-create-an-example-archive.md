# How do I use the Unix tar command to create an example archive?
// plain

The `tar` command is used to create and manipulate archives in Unix systems. To create an example archive, you can use the following command:

```
tar -cvf example.tar file1 file2
```

This command will create an archive named `example.tar` containing the files `file1` and `file2`.

The parts of the command are:
- `tar`: the command to create and manipulate archives
- `-cvf`: the options for the command, in this case `-c` for create, `-v` for verbose (to show the progress of the command), and `-f` for file (to specify the name of the archive)
- `example.tar`: the name of the archive
- `file1` and `file2`: the files to be included in the archive

For more information, see the [man page for tar](https://linux.die.net/man/1/tar).

onelinerhub: [How do I use the Unix tar command to create an example archive?](https://onelinerhub.com/cli-tar/how-do-i-use-the-unix-tar-command-to-create-an-example-archive)