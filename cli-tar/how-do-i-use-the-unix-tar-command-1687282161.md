# How do I use the Unix tar command?
// plain

The Unix `tar` command is used to create, extract, and manipulate files and directories in an archive format.

To create an archive, use the following command:
```
tar -cvf archive.tar directory_name
```
This command will create an archive called `archive.tar` that contains all the files and directories in `directory_name`.

To extract an archive, use the following command:
```
tar -xvf archive.tar
```
This command will extract all the files and directories in `archive.tar` into the current working directory.

To list the contents of an archive, use the following command:
```
tar -tvf archive.tar
```
This command will list the contents of `archive.tar` in the terminal.

The `tar` command has many other options that can be used to modify the behavior of the command. For more information, see the [GNU tar Manual](https://www.gnu.org/software/tar/manual/tar.html).

onelinerhub: [How do I use the Unix tar command?](https://onelinerhub.com/cli-tar/how-do-i-use-the-unix-tar-command-1687282161)