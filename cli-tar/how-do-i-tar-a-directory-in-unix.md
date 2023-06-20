# How do I tar a directory in Unix?
// plain

To tar a directory in Unix, use the `tar` command. The syntax for the command is `tar -cvf <name of tar file>.tar <name of directory>`. This command will create a tar file of the given directory.

For example:
```
tar -cvf my_directory.tar my_directory
```

This command will create a tar file called `my_directory.tar` with the contents of the directory `my_directory`.

The parts of the command are as follows:

* `tar` - the tar command
* `-cvf` - flags for the tar command, which stands for create, verbose, and file
* `my_directory.tar` - the name of the tar file to be created
* `my_directory` - the name of the directory to be tarred

## Helpful links

* [tar command manual](https://linux.die.net/man/1/tar)
* [tar command tutorial](https://www.computerhope.com/unix/utar.htm)

onelinerhub: [How do I tar a directory in Unix?](https://onelinerhub.com/cli-tar/how-do-i-tar-a-directory-in-unix)