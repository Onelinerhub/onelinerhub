# How can I use the shell tar command?
// plain

The `tar` command is a powerful tool for archiving and compressing files and directories. It is most commonly used in Linux and Unix-based operating systems, but can also be used with Windows. Here is an example of how to use the `tar` command to compress a directory:

```
$ tar -czvf my_directory.tar.gz my_directory
```

This command will create a `.tar.gz` file that contains all of the contents of `my_directory`. The `-c` flag tells the `tar` command to create an archive, the `-z` flag tells it to compress the archive using gzip, the `-v` flag tells it to be verbose (print the names of the files it is archiving), and the `-f` flag tells it to use the `my_directory.tar.gz` file as the archive.

The following list explains the parts of the command:
- `tar`: The command to create an archive
- `-c`: Tells the `tar` command to create an archive
- `-z`: Tells the `tar` command to compress the archive using gzip
- `-v`: Tells the `tar` command to be verbose (print the names of the files it is archiving)
- `-f`: Tells the `tar` command to use the `my_directory.tar.gz` file as the archive
- `my_directory.tar.gz`: The name of the archive file
- `my_directory`: The name of the directory to be archived

For more information on the `tar` command, see [this page](https://www.computerhope.com/unix/utar.htm).

onelinerhub: [How can I use the shell tar command?](https://onelinerhub.com/cli-tar/how-can-i-use-the-shell-tar-command)