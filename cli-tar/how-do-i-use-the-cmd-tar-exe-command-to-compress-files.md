# How do I use the cmd tar.exe command to compress files?
// plain

The `tar.exe` command is a Windows command line utility that allows you to create and manipulate tar archives. It can be used to compress files for storage or to transfer them over the internet.

The syntax for using `tar.exe` to compress files is:

```
tar.exe -cvf <archive_name.tar> <file_name>
```

This command will create a tar archive named `archive_name.tar` containing the file `file_name`.

The `-c` flag tells `tar.exe` to create a new archive.
The `-v` flag tells `tar.exe` to display the progress of the operation.
The `-f` flag tells `tar.exe` to use the following argument as the archive filename.

You can also compress multiple files into a single archive by listing them after the archive filename:

```
tar.exe -cvf <archive_name.tar> <file_1> <file_2> <file_3>
```

This command will create a tar archive named `archive_name.tar` containing the files `file_1`, `file_2`, and `file_3`.

More information about the `tar.exe` command can be found in the [Microsoft documentation](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/tar).

onelinerhub: [How do I use the cmd tar.exe command to compress files?](https://onelinerhub.com/cli-tar/how-do-i-use-the-cmd-tar-exe-command-to-compress-files)